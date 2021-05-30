# __hash__() % ((sys.maxsize + 1) * 2)
import json
import sys
import email
import hashlib
from os import walk
from os.path import join

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


def calculate_id(email_client):
    hash = email_client.__hash__() % ((sys.maxsize + 1) * 2)
    id = int(round(hash / 1111118111111))


    num_to_list = list(map(int, str(id)))
    aux = 8 - len(num_to_list)
    num_to_list += [0] * aux
    d0 = (num_to_list[0] + num_to_list[1]) % 10
    d1 = (num_to_list[2] + num_to_list[3]) % 10
    d2 = (num_to_list[4] + num_to_list[5]) % 10
    d3 = (num_to_list[6] + num_to_list[7]) % 10
    d4 = (num_to_list[3] + num_to_list[1]) % 10
    d5 = (num_to_list[5] + num_to_list[2]) % 10
    d6 = (num_to_list[4] + num_to_list[7]) % 10


    new_id = d6 * 100000 + d5 * 100000 + d4 * 10000 + d3 * 1000 + d2 * 100 + d1 * 10 + d0
    return new_id


if __name__ == "__main__":
    emails = read_mail_folder("./datasets/")
    domains = list(dict.fromkeys([email.get_sender_domain() for email in emails]))
    domain_indexes = {}
    for i in range(len(domains)):
        domain_indexes[domains[i]] = i

    domain_hashes = [int(round(domain.__hash__() % ((sys.maxsize + 1) * 2) / 1111118111111)) for domain in domains]
    short_domain_hashes = list(
        dict.fromkeys(
            domain_hashes
        )
    )
    print("Completo: ", len(domains))
    print("Sin repetir: ", len(short_domain_hashes))

# Con solo 4 digitos
# Completo:  7446
# Sin repetir:  5093

#  new_id =  d4 * 10000 + d3 * 1000 + d2 * 100 + d1 * 10 + d0
# Completo:  7446
# Sin repetir:  7174

#     new_id = d5 * 100000 + d4 * 10000 + d3 * 1000 + d2 * 100 + d1 * 10 + d0
# Completo:  7446
# Sin repetir:  7415 31

# cesar
# Completo:  7446
# Sin repetir:  7444
