from queue import PriorityQueue

def a_star_search(graph, start, goal):
    frontier = PriorityQueue()  # Priority queue ordered by total cost (g + h)
    frontier.put((0, start))  # Add start node with total cost 0
    came_from = {}  # Dictionary to store the parent of each node in the path
    cost_so_far = {start: 0}  # Dictionary to store the cost from start to each node

    while not frontier.empty():
        _, current = frontier.get()  # Get node with lowest total cost
        if current == goal:
            # Reconstruct path
            path = [current]
            while current != start:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path  # Return the path from start to goal
          
        for neighbor in graph[current]:
            new_cost = cost_so_far[current] + graph[current][neighbor]  # Calculate the new cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                total_cost = new_cost + heuristic(neighbor, goal)  # Calculate total cost (g + h)
                frontier.put((total_cost, neighbor))
                came_from[neighbor] = current  # Update the parent of the neighbor

    return None  # Goal not found

def heuristic(node, goal):
    # Example heuristic: Alphabet difference
    return abs(ord(node) - ord(goal))

# Example graph represented as adjacency list with alphabets and costs
graph = {
    'A': {'B': 1, 'D': 3},
    'B': {'A': 1, 'C': 2},
    'C': {'B': 2, 'F': 5},
    'D': {'A': 3, 'E': 1},
    'E': {'D': 1, 'F': 2},
    'F': {'C': 5, 'E': 2}
}

start_node = input("Enter start node (A-F): ").upper()
goal_node = input("Enter goal node (A-F): ").upper()

path = a_star_search(graph, start_node, goal_node)
if path:
    print("Path found:", ' -> '.join(path))
    print("Goal reached!")
else:
    print("Goal not reachable!")
