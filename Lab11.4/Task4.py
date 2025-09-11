class Node:
    """Represents a node in a binary search tree."""

    def __init__(self, data):
        """Initialize node with data and left/right pointers."""
        self.data = data
        self.left = None
        self.right = None

class BST:
    """Binary Search Tree implementation."""

    def __init__(self):
        """Initialize an empty BST."""
        self.root = None

    def insert(self, data):
        """Insert a new value into the BST.

        Args:
            data: Value to insert.
        """
        self.root = self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        """Helper method to insert recursively."""
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        elif data > node.data:
            node.right = self._insert_recursive(node.right, data)
        # If data == node.data, do not insert duplicates
        return node

    def search(self, value):
        """Search for a value in the BST.

        Args:
            value: Value to search for.

        Returns:
            True if found, False otherwise.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """Helper method to search recursively."""
        if node is None:
            return False
        if value == node.data:
            return True
        elif value < node.data:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder_traversal(self):
        """Return the inorder traversal of the BST as a list.

        Returns:
            List of node values in sorted order.
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """Helper method for inorder traversal."""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)

# Sample test code
if __name__ == "__main__":
    bst = BST()
    nums = [7, 3, 9, 1, 5, 8, 10]
    for num in nums:
        bst.insert(num)

    print("Inorder traversal:", bst.inorder_traversal())  # [1, 3, 5, 7, 8, 9, 10]

    # Test search for present and absent elements
    print("Search 5:", bst.search(5))   # True
    print("Search 11:", bst.search(11)) # False