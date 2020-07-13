def test_swap_every_other_node_iter():
    a = LinkNode(1)
    b = LinkNode(2)
    c = LinkNode(3)
    d = LinkNode(4)

    a.next = b
    b.next = c
    c.next = d

    assert a.data == 1
    assert b.data == 2
    assert c.data == 3
    assert d.data == 4


class LinkNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


a = LinkNode(1)
b = LinkNode(2)
c = LinkNode(3)
d = LinkNode(4)


a.next = b
b.next = c
c.next = d

current_node = a

i = 0

while current_node is not None:
    if i % 2 == 0:
        current_node.data, current_node.next.data = (
            current_node.next.data,
            current_node.data,
        )
    i += 1
    current_node = current_node.next

current_node = a
while current_node is not None:
    print(current_node.data)
    current_node = current_node.next
