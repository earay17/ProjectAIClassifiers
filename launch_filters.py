import email
import json
from os import walk
from os.path import join
from spamfilter import RandomForestFilter
from spamfilter.EmailEnvelope import EmailEnvelope
from spamfilter.NaiveBayesFilter import NaiveBayesFilter
from spamfilter.SVMPolyFilter import SVMPolyFilter
from spamfilter.SVMRBFFilter import SVMRBFFilter
from spamfilter.SVMSigmoidFilter import SVMSigmoidFilter


def read_mail(location: str):
    for path, dirs, files in walk(location):
        for file in files:
            try:
                with open(join(path, file)) as opened_file:
                    email_msg = email.message_from_file(opened_file)
                envelope = EmailEnvelope(
                    peer=None, mail_from=None, rcpt_tos=None,
                    email_msg=email_msg
                )
            except Exception as e:
                print("Error ", e)
                print("File: ", file)
    print("Loaded email from ", location)
    return envelope

filters = [NaiveBayesFilter, RandomForestFilter, SVMRBFFilter, SVMSigmoidFilter, SVMPolyFilter]
email_to_predict = read_mail("./datasets/test")

for filter in filters:
    filename = './generated/' + filter.__name__ + '.json'
    with open(filename, "r") as file:
        data = json.load(file)
    filter_object = filter()
    filter_object.set_initial_data(data)
    print(filter.__name__, ' : ', filter_object.filter(email_to_predict))
