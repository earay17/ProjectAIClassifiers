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


def read_mail_folder(location: str):
    """
    This function read all the emails from a path and parse each of them to EmailMessage
    :param location: path
    :return: Sequence[EmailMessage]
    """
    emails = list()
    for path, dirs, files in walk(location):
        for file in files:
            try:
                with open(join(path, file)) as opened_file:
                    email_msg = email.message_from_file(opened_file)
                envelope = EmailEnvelope(
                    peer=None, mail_from=None, rcpt_tos=None,
                    email_msg=email_msg
                )
                emails.append(envelope)
            except Exception as e:
                print("Error ", e)
                print("File: ", file)
    print("Loaded emails from ", location, ":", len(emails))
    return emails


filters = [NaiveBayesFilter, RandomForestFilter, SVMRBFFilter, SVMSigmoidFilter, SVMPolyFilter]
emails_to_predict = read_mail_folder("./datasets/test")

for filter in filters:
    # Read filter data
    filename = './generated/' + filter.__name__ + '.json'
    with open(filename, "r") as file:
        data = json.load(file)
    # Create filter
    filter_object = filter()
    filter_object.set_initial_data(data)
    # Do predictions
    for email in emails_to_predict:
        print(filter.__name__, ' : ', filter_object.filter(email))
