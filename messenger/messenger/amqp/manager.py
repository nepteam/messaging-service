from messenger.amqp.consumer  import Consumer
from messenger.amqp.publisher import Publisher
from pika.adapters.blocking_connection import BlockingConnection


class Manager(object):
    def __init__(self, parameters, connection_type=None, default_queue=None,
                 default_queue_options=None, share_connection=False):
        self._parameters      = parameters
        self._connection_type = connection_type or BlockingConnection
        self._connections     = {}
        self._channels        = {}
        self._default_queue   = default_queue
        self._default_queue_options = default_queue_options

    def connection(self, id):
        if id not in self._connections:
            self._connections[id] = self._connection_type(self._parameters)

        if not self._connections[id].is_open:
            self._connections[id].connect()

        return self._connections[id]

    def channel(self, id):
        if id not in self._channels:
            self._channels[id] = self.connection(id).channel()

        if not self._channels[id].is_open:
            self.connection(id)
            self._channels[id].open()

        return self._channels[id]

    def agent(self, id, kind):
        agent = kind(self.channel(id))

        if self._default_queue:
            agent.set_queue(self._default_queue)

        if self._default_queue_options:
            agent.set_options(self._default_queue_options)

        return agent

    def publisher(self, id=None):
        return self.agent(id, Publisher)

    def consumer(self, id=None):
        return self.agent(id, Consumer)