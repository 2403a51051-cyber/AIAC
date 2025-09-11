from collections import deque

class Graph:
    """Graph implementation using an adjacency list."""

    def __init__(self):
        """Initialize an empty adjacency list."""
        self.adj_list = {}

    def add_edge(self, src, dest):
        """Add an edge from src to dest (undirected).

        Args:
            src: Source node.
            dest: Destination node.
        """
        if src not in self.adj_list:
            self.adj_list[src] = []
        if dest not in self.adj_list:
            self.adj_list[dest] = []
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)  # Remove for directed graph

    def bfs(self, start):
        """Breadth-First Search traversal from start node.

        Args:
            start: Starting node.

        Returns:
            List of nodes in BFS order.
        """
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                result.append(node)
                visited.add(node)
                # Add all unvisited neighbors to the queue
                for neighbor in self.adj_list.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        return result

    def dfs_iterative(self, start):
        """Iterative Depth-First Search traversal from start node.

        Args:
            start: Starting node.

        Returns:
            List of nodes in DFS order.
        """
        visited = set()
        stack = [start]
        result = []

        while stack:
            node = stack.pop()
            if node not in visited:
                result.append(node)
                visited.add(node)
                # Add neighbors to stack (reverse for consistent order)
                for neighbor in reversed(self.adj_list.get(node, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result

    def dfs_recursive(self, start):
        """Recursive Depth-First Search traversal from start node.

        Args:
            start: Starting node.

        Returns:
            List of nodes in DFS order.
        """
        result = []
        visited = set()

        def dfs(node):
            if node not in visited:
                result.append(node)
                visited.add(node)
                # Recursively visit all unvisited neighbors
                for neighbor in self.adj_list.get(node, []):
                    dfs(neighbor)

        dfs(start)
        return result

# Sample test code
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'E')
    g.add_edge('D', 'E')

    print("Adjacency List:", g.adj_list)
    print("BFS from A:", g.bfs('A'))                # ['A', 'B', 'C', 'D', 'E']
    print("Iterative DFS from A:", g.dfs_iterative('A'))  # ['A', 'C', 'E', 'D', 'B'] or similar
    print("Recursive DFS from A:", g.dfs_recursive('A'))  # ['A', 'B', 'D', 'E',