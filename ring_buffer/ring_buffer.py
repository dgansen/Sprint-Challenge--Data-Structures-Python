class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.old_idx = 0

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.storage[self.old_idx] = item
            self.old_idx = self.old_idx+1 if self.old_idx+1 < len(self.storage) else 0
        else:
            self.storage.append(item)

    def get(self):
        return self.storage