import LQueue as q


class QueueOutOfRangeException(Exception):
    pass


class ConversionError(Exception):
    pass


class ImprovedQueue(q.LQueue):
    queues_dict = {}

    def __init__(self, size, name):
        super().__init__()
        self.name = name
        if isinstance(size, int):
            self.size = size
        else:
            raise ConversionError(size, type(size), "size should be of type int")

        self.queues_dict[self.name] = {"size": self.size, "data": self.lqueue}

    def insert(self, item):
        if len(self.lqueue) < self.size:
            super().insert(item)
        else:
            raise QueueOutOfRangeException(self.size)

    @classmethod
    def get_queue(cls, name):
        if cls.queues_dict[name]:
            return cls.queues_dict[name]
        return None
