class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enque(self, item):
        self.items.append(item)
    def deque(self):
        return self.items.pop(0)
    def peek(self):
        return self.items[0]
    def size(self):
        return len(self.items)