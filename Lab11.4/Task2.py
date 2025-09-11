from collections import deque

class ListQueue:
    """Queue implementation using Python lists.

    Methods:
        enqueue(item): Add item to the end of the queue.
        dequeue(): Remove and return item from the front.
        is_empty(): Check if the queue is empty.
    """

    def __init__(self):
        """Initialize an empty queue."""
        self.items = []

    def enqueue(self, item):
        """Add item to the end of the queue.

        Args:
            item: Item to add.
        """
        self.items.append(item)

    def dequeue(self):
        """Remove and return item from the front.

        Returns:
            The item at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        # Removing from front of list is O(n)
        return self.items.pop(0)

    def is_empty(self):
        """Check if the queue is empty.

        Returns:
            True if empty, False otherwise.
        """
        return len(self.items) == 0

class DequeQueue:
    """Queue implementation using collections.deque.

    Methods:
        enqueue(item): Add item to the end of the queue.
        dequeue(): Remove and return item from the front.
        is_empty(): Check if the queue is empty.
    """

    def __init__(self):
        """Initialize an empty queue."""
        self.items = deque()

    def enqueue(self, item):
        """Add item to the end of the queue.

        Args:
            item: Item to add.
        """
        self.items.append(item)

    def dequeue(self):
        """Remove and return item from the front.

        Returns:
            The item at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        # Removing from front of deque is O(1)
        return self.items.popleft()

    def is_empty(self):
        """Check if the queue is empty.

        Returns:
            True if empty, False otherwise.
        """
        return len(self.items) == 0

# Performance Comparison:
# - ListQueue: enqueue is O(1), dequeue is O(n) due to pop(0) shifting elements.
# - DequeQueue: both enqueue and dequeue are O(1), making it more efficient for large queues.

# Sample test code
if __name__ == "__main__":
    print("Testing ListQueue:")
    q1 = ListQueue()
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)
    print(q1.dequeue())  # 1
    print(q1.is_empty()) # False

    print("\nTesting DequeQueue:")
    q2 = DequeQueue()
    q2.enqueue(1)
    q2.enqueue(2)
    q2.enqueue(3)
    print(q2.dequeue())  # 1
    print(q2.is_empty()) #