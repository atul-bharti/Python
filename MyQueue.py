class MyQueue:
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


    def reverse(self):
        element = None
        if self.size() == 1:
            return
        element = self.deque()
        self.reverse()
        self.enque(element)
'''
queue = MyQueue()
queue.enque(1)
queue.enque(2)
queue.enque(3)
queue.enque(4)
queue.enque(5)
print(queue.items)

queue.reverse()
print('After Reverse')

print(queue.items)
'''