from messenger.amqp.base import Base
from messenger.amqp.exception import UndefinedQueueError


class Publisher(Base):
    def publish(self, message, route=None, **kwargs):
        if not self._queue:
            raise UndefinedQueueError('Queue is not defined.')

        self._kwargs = kwargs
        self._queue  = route or self._queue

        self._kwargs.update({
            'routing_key': route or self._queue,
            'body':        message
        })

        if 'exchange' not in self._kwargs:
            self._kwargs['exchange'] = ''

        self.start()

    def run(self):
        self._channel.queue_declare(queue=self._queue, **self._queue_options)
        self._channel.basic_publish(**self._kwargs)