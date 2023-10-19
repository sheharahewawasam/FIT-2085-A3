from data_structures.referential_array import ArrayR, T
from data_structures.stack_adt import Stack

class ArrayStack(Stack[T]):
    """Implementation of a stack with arrays.

    This class implements a stack data structure using arrays.

    Attributes:
        MIN_CAPACITY (int): The minimum capacity for the underlying array.

    """

    MIN_CAPACITY = 1

    def __init__(self, max_capacity: int) -> None:
        """
        Initialize the ArrayStack with a maximum capacity.

        Args:
            max_capacity (int): The maximum capacity of the stack.

        """
        Stack.__init__(self)
        self.array = ArrayR(max(max_capacity, self.MIN_CAPACITY))

    def is_full(self) -> bool:
        """
        Check if the stack is full.

        Returns:
            bool: True if the stack is full, False otherwise.

        """
        return len(self) == len(self.array)

    def push(self, item: T) -> None:
        """
        Push an item onto the stack.

        Args:
            item (T): The item to push onto the stack.

        Raises:
            Exception: If the stack is full, an exception is raised.

        """
        if self.is_full():
            raise Exception("Stack is full")
        self.array[len(self)] = item
        self.length += 1

    def pop(self) -> T:
        """
        Pop an item from the stack.

        Returns:
            T: The item popped from the stack.

        Raises:
            Exception: If the stack is empty, an exception is raised.

        """
        if self.is_empty():
            raise Exception("Stack is empty")
        self.length -= 1
        return self.array[self.length]

    def peek(self) -> T:
        """
        Peek at the top item on the stack without removing it.

        Returns:
            T: The top item on the stack.

        Raises:
            Exception: If the stack is empty, an exception is raised.

        """
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.array[self.length - 1]
