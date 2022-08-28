from framework.events import subscribe
from framework.events import post_event


def create_account(*args):
    print(f"Created Account : {args[0]} ")


def debit(*args):
    print(f"debited {args[0]} amount !!")
    post_event("send_mail",args[0])


def setup_account():
    subscribe("create_account", create_account)
    subscribe("debit", debit)
