"""
Remove duplictes from an unsorted linked list.
"""


class LinkedNodes:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


a = LinkedNodes(5)
b = LinkedNodes(4)
c = LinkedNodes(5)

a.next = b
b.next = c

head_node = a


def remove_duplicates(head_node):
    current_node = head_node
    previous = None
    seen_numbers = set()

    while current_node is not None:
        if current_node.data not in seen_numbers:
            seen_numbers.add(current_node.data)
            previous, current_node = current_node, current_node.next
        else:
            current_node, previous.next = previous.next, current_node.next


remove_duplicates(head_node)

current_node = a
while current_node is not None:
    print(current_node.data)
    current_node = current_node.next
