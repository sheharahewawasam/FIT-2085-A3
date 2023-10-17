from data_structures.referential_array import ArrayR, T
from data_structures.stack_adt import Stack

class ArrayStack(Stack[T]):
    """ Implementation of a stack with arrays.
    """
    MIN_CAPACITY = 1

    def __init__(self, max_capacity: int) -> None:

        Stack.__init__(self)
        self.array = ArrayR(max(self.MIN_CAPACITY, max_capacity))

    def is_full(self) -> bool:

        return len(self) == len(self.array)

    def push(self, item: T) -> None:
        if self.is_full():
            raise Exception("Stack is full")
        self.array[len(self)] = item
        self.length += 1

    def pop(self) -> T:
        if self.is_empty():
            raise Exception("Stack is empty")
        self.length -= 1
        return self.array[self.length]

    def peek(self) -> T:
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.array[self.length-1]