"""
ring_buffer.py

Models a ring buffer.
"""

import stdarray
import stdio
import sys


def create(capacity):
    """
    Create and return a ring buffer, with the given maximum capacity and
    with all elements initialized to None. A ring buffer is represented as
    a list of four elements: the buffer (buff) itself as a list; number of
    elements (size) currently in buff; the index (first) of the least
    recently inserted item; and the index (last) one beyond the most recently
    inserted item.
    """

    buff = stdarray.create1D(capacity, None)

    first = 0
    last = 0
    size = 0
    ring_buffer = [buff, size, first, last]
    return ring_buffer


def capacity(rb):
    """
    Return the capacity of the ring buffer.
    """

    buff = rb[0]
    return len(buff)


def size(rb):
    """
    Return the number of items currently in the buffer rb.
    """

    size = rb[1]
    return size


def is_empty(rb):
    """
    Return True if the buffer rb is empty and False otherwise.
    """

    buff = rb[0]
    for i in range(0, capacity(buff)):
        if buff[i] is None:
            return False
    return True


def is_full(rb):
    """
    Return True if the buffer rb is full and False otherwise.
    """

    return size(rb) == capacity(rb)


def enqueue(rb, x):
    """
    Add item x to the end of the buffer rb.
    """

    last = rb[3]
    rb[0][last] = x

    last += 1
    if last == capacity(rb):
        last = 0
    rb[1] += 1
    rb[3] = last


def dequeue(rb):
    """
    Delete and return item from the front of the buffer rb.
    """

    first = rb[2]
    v = rb[0][first]
    first += 1
    if first == capacity(rb):
        first = 0
    rb[2] = first
    rb[1] -= 1
    return v


def peek(rb):
    """
    Return (but do not delete) item from the front of the buffer rb.
    """

    first = rb[2]
    return rb[0][first]


def _main():
    """
    Test client [DO NOT EDIT].
    """

    N = int(sys.argv[1])
    rb = create(N)
    for i in range(1, N + 1):
        enqueue(rb, i)
    t = dequeue(rb)
    enqueue(rb, t)
    stdio.writef('Size after wrap-around is %d\n', size(rb))
    while size(rb) >= 2:
        x = dequeue(rb)
        y = dequeue(rb)
        enqueue(rb, x + y)
    stdio.writeln(peek(rb))


if __name__ == '__main__':
    _main()
