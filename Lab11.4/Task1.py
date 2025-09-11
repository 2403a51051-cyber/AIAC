class Stack:
    """A simple Stack (LIFO) implementation.

    Methods:
        push(item): Add an item to the top of the stack.
        pop(): Remove and return the top item of the stack.
        peek(): Return the top item without removing it.
        is_empty(): Check if the stack is empty.
    """

    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack.

        Args:
            item: The item to be added.
        """
        self.items.append(item)

    def pop(self):
        """Remove and return the top item of the stack.

        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it.

        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        """Check if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

# Sample test code
if __name__ == "__main__":
    stack = Stack()
    print("Is empty?", stack.is_empty())  # True
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Peek:", stack.peek())          # 30
    print("Pop:", stack.pop())            # 30
    print("Peek after pop:", stack.peek())# 20
    print("Is empty?", stack.is_empty())  # False