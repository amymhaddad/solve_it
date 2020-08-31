from unique_email import number_unique_emails

emails = [
    "test.email+alex@leetcode.com",
    "test.e.mail+bob.cathy@leetcode.com",
    "testemail+david@lee.tcode.com",
]


def test_number_unique_emails():
    assert number_unique_emails(emails) == 2
