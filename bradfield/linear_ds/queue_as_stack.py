"""
Implement a queue using stacks.Although this problem might seem contrived, implementing a queue using stacks is actually a common strategy in functional programming languages (such as Haskell or Standard ML) where stacks are much more convenient to implement “from scratch” than queues. Your solution should have the same interface as the queue implementation in algos, but use stacks instead of a list in the implementation.
"""
from stack import Stack


item = 1


class QueueAsStack(object):
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, item):

        self.s1.push(item)

    def dequeue(self):
        if self.s2.is_empty():
            while not self.s1.is_empty():
                last_item = self.s1.pop()
                self.s2.push(last_item)
        return self.s2.pop()


q1 = QueueAsStack()
q1.enqueue(item)
print(q1.dequeue())
