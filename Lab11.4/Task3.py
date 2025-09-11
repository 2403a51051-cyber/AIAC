class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, data):
        """Initialize node with data and next pointer."""
        self.data = data
        self.next = None

class LinkedList:
    """Singly linked list implementation."""

    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def insert_at_end(self, data):
        """Insert a new node with the given data at the end of the list.

        Args:
            data: Data to store in the new node.
        """
        new_node = Node(data)
        if not self.head:
            # If list is empty, new node becomes head
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        # Set the next pointer of the last node to new_node
        current.next = new_node

    def delete_value(self, value):
        """Delete the first node with the specified value.

        Args:
            value: Value to delete from the list.

        Raises:
            ValueError: If value is not found.
        """
        current = self.head
        prev = None
        while current:
            if current.data == value:
                if prev:
                    # Bypass the current node by updating prev.next
                    prev.next = current.next
                else:
                    # If head needs to be deleted, move head pointer
                    self.head = current.next
                return
            prev = current
            current = current.next
        raise ValueError(f"{value} not found in list")

    def traverse(self):
        """Traverse the list and return elements as a list.

        Returns:
            List of node data.
        """
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Suggested test cases
if __name__ == "__main__":
    ll = LinkedList()
    # Test insertions
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    print("After insertions:", ll.traverse())  # [1, 2, 3]

    # Test deletion of middle value
    ll.delete_value(2)
    print("After deleting 2:", ll.traverse())  # [1, 3]

    # Test deletion of head
    ll.delete_value(1)
    print("After deleting 1:", ll.traverse())  # [3]

    # Test deletion of last value
    ll.delete_value(3)
    print("After deleting 3:", ll.traverse())  # []

    # Test deletion of non-existent value (should raise ValueError)
    try:
        ll.delete_value(99)
    except ValueError as e:
        print("Error:", e)  # 99 not found in list False