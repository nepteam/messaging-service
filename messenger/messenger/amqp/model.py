from time import time

class Message(object):
    def __init__(self, sender, owner, recipients, body, kind, created=None, is_read=False):
        self.sender = sender
        self.owner  = owner
        self.kind   = kind
        self.body   = body
        self.recipients = recipients
        self.created = created or time()
        self.is_read = is_read