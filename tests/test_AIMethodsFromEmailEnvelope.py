import sys
from unittest import TestCase
from os.path import join
from os import walk
import email

from spamfilter.EmailEnvelope import EmailEnvelope


class AIMethodsFromEmailEnvelope(TestCase):
    email1: EmailEnvelope = None
    email2: EmailEnvelope = None
    email3: EmailEnvelope = None

    def __init__(self, *args, **kwargs):
        """
        This constructor call parent constructor and initialize de emails
        that are going to be tested
        :param args:
        :param kwargs:
        """
        # Call parent constructor
        super(AIMethodsFromEmailEnvelope, self).__init__(*args, **kwargs)
        file = open("email_for_test/email_test.eml")
        msg = email.message_from_file(file)
        self.email1 = EmailEnvelope(
            peer=None, mail_from=None, rcpt_tos=None,
            email_msg=msg
        )
        file = open("email_for_test/email2_test.eml")
        msg = email.message_from_file(file)
        self.email2 = EmailEnvelope(
            peer=None, mail_from=None, rcpt_tos=None,
            email_msg=msg
        )
        file = open("email_for_test/email3_test.eml")
        msg = email.message_from_file(file)
        self.email3 = EmailEnvelope(
            peer=None, mail_from=None, rcpt_tos=None,
            email_msg=msg
        )

    def test_ai_check_count_urls(self):
        self.assertEqual(self.email1.ai_check_count_urls(), 4)
        self.assertEqual(self.email2.ai_check_count_urls(), 14)
        self.assertEqual(self.email3.ai_check_count_urls(), 0)

    def test_ai_check_count_images(self):
        self.assertEqual(self.email1.ai_check_count_images(), 0)
        self.assertEqual(self.email2.ai_check_count_images(), 7)
        self.assertEqual(self.email3.ai_check_count_images(), 0)

    def test_get_content_type_frequencies(self):
        self.assertEqual(self.email1.get_content_type_frequencies().get('text/html'), 2)
        self.assertEqual(self.email1.get_content_type_frequencies().get('multipart/mixed'), 1)
        self.assertEqual(self.email2.get_content_type_frequencies().get('multipart/alternative'), 1)
        self.assertEqual(self.email2.get_content_type_frequencies().get('text/plain'), 1)
        self.assertEqual(self.email2.get_content_type_frequencies().get('text/html'), 1)

    def test_get_extension_frequencies(self):
        self.assertEqual(self.email1.get_extension_frequencies().get('PDF.html'), 1)
        self.assertEqual(self.email3.get_extension_frequencies().get('zip'), 1)

    def test_ai_check_email_client_id(self):
        self.assertEqual(self.email1.ai_check_email_client_id(),
                         int(round('hubersuhner.com'.__hash__() % ((sys.maxsize + 1) * 2) / 1111118111111)))
        self.assertEqual(self.email2.ai_check_email_client_id(),
                         int(round('insurancemail.net'.__hash__() % ((sys.maxsize + 1) * 2) / 1111118111111)))
        self.assertEqual(self.email3.ai_check_email_client_id(),
                         int(round('psassessoria.com'.__hash__() % ((sys.maxsize + 1) * 2) / 1111118111111)))

    def test_ai_check_return_path_equals_from_or_tos(self):
        self.assertEqual(self.email1.ai_check_return_path_equals_from_or_tos(), 0)
        self.assertEqual(self.email2.ai_check_return_path_equals_from_or_tos(), 0)
        self.assertEqual(self.email3.ai_check_return_path_equals_from_or_tos(), 0)

    def test_ai_check_from_equals_reply_to(self):
        self.assertEqual(self.email1.ai_check_from_equals_reply_to(), 1)
        self.assertEqual(self.email2.ai_check_from_equals_reply_to(), 0)
        self.assertEqual(self.email3.ai_check_from_equals_reply_to(), 0)
