import heapq

def dijkstra(graph, source):
    """
    Dijkstra's algorithm for finding shortest paths from source to all nodes.
    
    Algorithm Steps:
    1. Initialize distances: source = 0, all others = infinity
    2. Create priority queue with (distance, node) tuples
    3. While queue is not empty:
       a. Extract node with minimum distance
       b. For each neighbor, perform edge relaxation
       c. If new path is shorter, update distance and add to queue
    
    Edge Relaxation Pattern:
    - Calculate new_distance = current_distance + edge_weight
    - If new_distance < distances[neighbor]:
        - Update distances[neighbor] = new_distance
        - Add (new_distance, neighbor) to priority queue
    
    Args:
        graph (dict): Adjacency dictionary {node: {neighbor: weight}}
        source (str): Starting node
        
    Returns:
        dict: Shortest distances from source to all nodes
    """
    if not graph or source not in graph:
        return {}
    
    # Step 1: Initialize distances
    distances = {node: float('infinity') for node in graph}
    distances[source] = 0  # Source distance is 0
    
    # Step 2: Priority queue (min-heap) with (distance, node) tuples
    priority_queue = [(0, source)]
    visited = set()
    
    # Step 3: Main algorithm loop
    while priority_queue:
        # Extract node with minimum distance
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Skip if already visited (optimization)
        if current_node in visited:
            continue
            
        visited.add(current_node)
        
        # Edge relaxation pattern
        for neighbor, weight in graph.get(current_node, {}).items():
            if neighbor not in visited:
                # Calculate new distance through current node
                new_distance = current_distance + weight
                
                # Relaxation: update if new path is shorter
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))
    
    return distances

def test_dijkstra():
    """Test cases for Dijkstra's algorithm."""
    
    test_cases = [
        # (graph, source, expected, description)
        ({'A': {'B': 1, 'C': 4}, 'B': {'C': 2, 'D': 5}, 'C': {'D': 1}, 'D': {}}, 'A', 
         {'A': 0, 'B': 1, 'C': 3, 'D': 4}, "Sample input"),
        ({'A': {'B': 3}, 'B': {'C': 2}, 'C': {'D': 1}, 'D': {}}, 'A',
         {'A': 0, 'B': 3, 'C': 5, 'D': 6}, "Linear graph"),
        ({'A': {}}, 'A', {'A': 0}, "Single node"),
        ({'A': {'B': 2}, 'B': {'A': 2}, 'C': {'D': 3}, 'D': {'C': 3}}, 'A',
         {'A': 0, 'B': 2, 'C': float('infinity'), 'D': float('infinity')}, "Disconnected"),
    ]
    
    print("Running Dijkstra tests...\n")
    all_passed = True
    
    for i, (graph, source, expected, desc) in enumerate(test_cases, 1):
        result = dijkstra(graph, source)
        passed = result == expected
        status = "✅ PASS" if passed else "❌ FAIL"
        
        print(f"Test {i}: {status} - {desc}")
        if not passed:
            print(f"  Expected: {expected}")
            print(f"  Got:      {result}")
            all_passed = False
        print()
    
    print("=" * 40)
    print("🎉 ALL TESTS PASSED!" if all_passed else "❌ SOME TESTS FAILED!")
    print("=" * 40)
    
    return all_passed

if __name__ == "__main__":
    # Get graph input from user
    print("Enter graph as dictionary:")
    graph_input = input("Graph: ").strip()
    
    # Get source node
    source = input("Enter source node: ").strip().upper()
    
    try:
        # Parse and process
        graph = eval(graph_input)
        distances = dijkstra(graph, source)
        
        # Format output exactly as specified
        output = "{"
        for i, (node, dist) in enumerate(distances.items()):
            if i > 0:
                output += ","
            output += f"'{node}':{int(dist) if dist != float('infinity') else 'inf'}"
        output += "}"
        
        print(output)
        
    except Exception as e:
        print(f"Error: {e}")
        
    # Uncomment to run tests: test_dijkstra()
