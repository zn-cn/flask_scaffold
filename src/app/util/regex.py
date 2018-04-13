import re

email_pat = re.compile(r'^[\d,a-z]([\w\.\-]+)@([a-z0-9\-]+).([a-z\.]+[a-z])$')


def check_email(email):
    return email_pat.match(email)