from queue import Queue


# if the operation cannot successfully complete because the queue is either empty (cant get) or full ( cant put).
# The default behavior is to block or idly wait until the Queue object has data or room available to
# complete the operation.
# You can have it raise exceptions instead by passing the block=False parameter.
# Or you can have it wait a defined amount of time before raising an exception by passing a timeout parameter

def fifo_ex():
    # FIFO
    lineup = Queue(maxsize=3)
    # lineup.get(block=False)
    lineup.put(1)
    lineup.put(2)
    lineup.put(3)
    # lineup.put(4, timeout=1)
    print('lineup.full():', lineup.full())
    print(lineup.get())
    print(lineup.get())
    print(lineup.get())
    print('lineup.empty():', lineup.empty())


def lifo_ex():
    # LIFO, also called stacks ()
    # Applicable situation - concurrent
    # why not use list
    from queue import LifoQueue
    stack = LifoQueue(maxsize=3)
    stack.put(1)
    stack.put(2)
    stack.put(3)
    # stack.put(4, block=False)
    print(stack.get())
    print(stack.get())
    print(stack.get())
    # stack.get(timeout=1)


def priority_queue_ex():
    # data structure - heap
    # Applicable situation - product recommendation
    from queue import PriorityQueue
    pq = PriorityQueue()
    pq.put((5, 'c'))
    pq.put((2, 'a'))
    pq.put((1, 'b'))
    pq.put((4, 'd'))
    while not pq.empty():
        print(pq.get())


def priority_queue_ex_2():
    from queue import PriorityQueue
    pq = PriorityQueue()
    pq.put((-5, 'c'))
    pq.put((-2, 'a'))
    pq.put((-1, 'b'))
    pq.put((-4, 'd'))
    while not pq.empty():
        print(pq.get())


if __name__ == "__main__":
    fifo_ex()
    # lifo_ex()
    # priority_queue_ex()
    # priority_queue_ex_2()
