from typing import Sequence
import numpy as np
from spamfilter.EmailEnvelope import EmailEnvelope


class MatrixGenerator:
    _matrix: np.array
    _emails: Sequence[EmailEnvelope] = None
    _spam_emails: Sequence[EmailEnvelope] = None
    _ham_emails: Sequence[EmailEnvelope] = None

    def __init__(self, spam_emails: Sequence[EmailEnvelope] = None, ham_emails: Sequence[EmailEnvelope] = None):
        if spam_emails is not None and ham_emails is not None:
            self._spam_emails = spam_emails
            self._ham_emails = ham_emails
            self._emails = self._spam_emails + self._ham_emails

    def calculate_matrix(self):
        """
        This function calculates two-dimensional list, the columns are the checks and de rows the union of spam and ham.
        Also prints the two-dimensional list in matrix format
        :param spam: sequence of spam EmailMessages
        :param ham: sequence of ham EmailMessages
        :param checks: criterias to check
        :return:  two-dimensional list
        """
        matrix = []
        len_spam = len(self._spam_emails)
        n_emails = len(self._emails)
        for email_index in range(n_emails):
            is_spam = 1 if 0 <= email_index < len_spam else 0
            # print(is_spam)
            email = self._emails[email_index]
            all_checks = email.ai_matrix_for_email()
            row = [is_spam] + all_checks
            matrix.append(row)
        self._matrix = np.array(matrix, dtype='uint64')

    def store_matrix(self, filename):
        header = ["label"] + EmailEnvelope.checks + EmailEnvelope.all_content_types + EmailEnvelope.all_extension_types
        np.savetxt(
            fname=filename, X=self._matrix, fmt='%s', delimiter=' ',
            newline='\n', header=str(header), footer='',
            comments='# ', encoding=None
        )
