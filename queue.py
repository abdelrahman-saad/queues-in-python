class LQueue:
    count = 0

    def __init__(self):
        LQueue.count += 1
        self.lqueue = []

    def insert(self, item):
        self.lqueue.append(item)

    def pop(self):
        if len(self.lqueue) != 0:
            return self.lqueue.pop(0)
        else:
            return None

    def is_empty(self):
        return False if len(self.lqueue) > 0 else True

    @classmethod
    def get_queues_count(cls):
        return cls.count
