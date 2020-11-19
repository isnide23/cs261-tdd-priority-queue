# NaivePriorityQueue (aka 'ShittyQueue'): A simple but inefficient priority queue.
# Your implementation should pass the tests in test_naive_priority_queue.py.
# Ian Snyder

class NaivePriorityQueue:

    def __init__(self):
        self.data = []
        self.size = 0

    def enqueue(self, value):
        self.data.append(value)
        self.size += 1

    def dequeue(self):
        self.data.sort()
        if self.is_empty() is False:
            self.size -= 1
            return self.data.pop()
        else:
            return None

    def is_empty(self):
        return self.size == 0

    
