import pytest 
from queue_with_stacks.queue_with_stacks import PseudoQueue, InvalidOperationError

# enqueue(value) which inserts value into the PseudoQueue, using a first-in, first-out approach.

def test_enqueue_fifo_method():
    q = PseudoQueue()
    q.enqueue(5)
    actual = q.rear.value
    expected = 5
    assert actual == expected

def test_enqueue_fifo_two_inputs():
    q = PseudoQueue()
    q.enqueue(5)
    q.enqueue(10)
    actual = q.rear.value
    expected = 5
    assert actual == expected

def test_enqueue_fifo_several_inputs():
    q = PseudoQueue()
    q.enqueue(5)
    q.enqueue(10)
    q.enqueue(15)
    q.enqueue(20)
    actual = q.rear.value
    expected = 5
    assert actual == expected
