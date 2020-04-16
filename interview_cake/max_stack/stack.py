class Stack(object):
    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]

    def is_empty(self):
        return bool(len(self.items) == 0)


#   def push(self, item):
#         """If maxes_stack is empty, then add item to max_stack.
#         If item is larger than the topmost item in maxes_stack, then remove the current max number.
#         Add item to max_stack.
#         """

#         if self.maxes_stack.is_empty():
#             self.maxes_stack.push(item)

#         elif item > self.maxes_stack.peek():
#             self.maxes_stack.pop()
#             self.maxes_stack.push(item)

#     def pop(self):
#         """Remove and return the top item from our stack."""
#         self.pop()

#     def peek(self):
#         """Return the last item without removing it"""
#         return self.maxes_stack.peek()

#     def get_max(self):
#         """Get largest number in stack"""
#         return self.maxes_stack.peek()
