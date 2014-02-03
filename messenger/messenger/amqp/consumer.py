from messenger.amqp.base import Base
from messenger.amqp.exception import UndefinedQueueError


class Consumer(Base):
    def consume(self, callback):
        if not self._queue:
            raise UndefinedQueueError('Queue is not defined.')

        self._kwargs = {
            'queue':             self._queue,
            'consumer_callback': callback
        }

        self.start()

    def abort(self):
        self._channel.stop_consuming()

    def run(self):
        self._channel.queue_declare(queue=self._queue, **self._queue_options)
        self._channel.basic_consume(**self._kwargs)
        self._channel.start_consuming()