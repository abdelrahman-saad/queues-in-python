import queue as q


class QueueOutOfRangeException(Exception):
    pass


class ImprovedQueue(q.LQueue):
    queues_dict = {}

    def __init__(self, size, name):
        super().__init__()
        self.name = name
        self.size = size
        self.queues_dict[self.name] = {"size": self.size, "data": self.lqueue}

    def insert(self, item):
        if len(self.lqueue) <= self.size:
            super().insert(item)
        else:
            raise QueueOutOfRangeException(self.size)

    def get_queue(self, name):
        if self.queues_dict[name]:
            return self.queues_dict[name]
        return None
