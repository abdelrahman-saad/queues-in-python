class LQueue:
    count = 0
    queues = []

    def __init__(self):
        LQueue.count += 1
        self.lqueue = []
        self.queues.append(self.lqueue)

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

    @classmethod
    def append_all(cls, items):
        cls.queues = items

    @classmethod
    def save(cls, filename):
        with open(filename, "w") as file:
            data_to_save = []
            for q in cls.queues:
                data_to_save.append(','.join(map(str, q)))
            file.write('\n'.join(data_to_save))

    @classmethod
    def load(cls, filename):
        new_queues = []

        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                queue_values = line.strip().split(',')
                lqueue = [value for value in queue_values]
                new_queues.append(lqueue)

        cls.queues = new_queues
        cls.count = len(new_queues)

        return new_queues

