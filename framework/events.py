subscribers = dict()


def subscribe(event_type: str, fn):
    subscribers[event_type]=fn


def post_event(event_type: str, data):
    subscribers[event_type](data)


