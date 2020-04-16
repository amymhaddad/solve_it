"""
You've already implemented a Stack class (below).

Create a MaxStack class and include a method get_max() that returns the largest element in the stack. get_max() should not remove the item.

Your stacks will contain only integers.
"""
from stack import Stack


class MaxStack(object):
    def __init__(self):
        self.main_stack = Stack()
        self.maxes_stack = Stack()

    def push(self, item):
        self.main_stack.push(item)

    def get_max(self):
        """Get largest number in stack"""

        while not self.main_stack.is_empty():
            main_stack_num = self.main_stack.pop()
            if self.maxes_stack.is_empty():
                self.maxes_stack.push(main_stack_num)
            else:
                maxes_stack_num = self.maxes_stack.peek()
                if main_stack_num > maxes_stack_num:
                    self.maxes_stack.push(main_stack_num)
        return self.maxes_stack.peek()


max_stack = MaxStack()
max_stack.push(4)
max_stack.push(7)
max_stack.push(7)
max_stack.push(8)
print(max_stack.get_max())
