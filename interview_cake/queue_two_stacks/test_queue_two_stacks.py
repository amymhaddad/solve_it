import pytest

from queue_two_stacks import QueueTwoStacks


def test_queue_two_stacks():
    queue = QueueTwoStacks()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3


def test_queue_two_stacks_with_a_pop_after_rotation():
    queue = QueueTwoStacks()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.dequeue() == 1

    queue.enqueue(4)

    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.dequeue() == 4
