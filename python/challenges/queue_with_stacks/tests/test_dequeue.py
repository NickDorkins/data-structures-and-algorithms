import pytest 
from queue_with_stacks.queue_with_stacks import PseudoQueue, InvalidOperationError


# dequeue() which extracts a value from the PseudoQueue, using a first-in, first-out approach.

def test_dequeue_fifo_method():
    q = PseudoQueue()
    q.enqueue(5)
    q.enqueue(10)
    actual = q.dequeue()
    expected = 5
    assert actual == expected

