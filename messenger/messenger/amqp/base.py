from threading import Thread

class Base(Thread):
    def __init__(self, channel):
        super(AMQPAgent, self).__init__()

        self._channel = channel
        self._queue   = None
        self._queue_options = {}
        self._kwargs  = {}

    def set_queue(self, queue):
        self._queue = queue

    def set_options(self, options):
        self._queue_options = options