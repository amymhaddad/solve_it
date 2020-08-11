"""
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
"""


class LinkedNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

a = LinkedNode(1)
b = LinkedNode(2)
c = LinkedNode(3)
d = LinkedNode(4)

a.next = b
b.next = c
c.next = d


def delete_node(node):
    current_node = node

    current_node.data = current_node.next.data
    current_node.next = current_node.next.next

current_node = delete_node(b)

current_node = a
while current_node is not None:
    print(current_node.data)
    current_node = current_node.next
