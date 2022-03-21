import email
import time
from os import walk
from os.path import join
from MatrixGenerator import MatrixGenerator
from spamfilter.EmailEnvelope import EmailEnvelope


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


# READ AND CREATE MATRIX
start_time = time.time()
print('New generate matrix')
print(f"Reading emails...")
spam_emails = read_mail_folder("./datasets/spam/")
ham_emails = read_mail_folder("./datasets/ham/")
print("Creating matrix...")
matrix = MatrixGenerator(spam_emails, ham_emails)
matrix.calculate_matrix()
print("Storing matrix...")
matrix.store_matrix('generated/matrix.csv')
total_time = time.time() - start_time
print("Total time: ", total_time)
