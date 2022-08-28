from framework.bank import setup_account
from framework.events import post_event
from framework.mail import setup_mail

setup_account()
setup_mail()

post_event("create_account","test")
post_event("debit",100)

