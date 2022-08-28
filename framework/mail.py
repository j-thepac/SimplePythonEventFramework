from framework.events import subscribe


def send_mail(*args):
    print(f"<< Mail : Amount {args[0]} has been deducted>>")


def setup_mail():
    subscribe("send_mail", send_mail)

