Input:
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, start, goal):
        max_vertex = max(max(self.graph), start, goal)
        visited = [False] * (max_vertex + 1)
        queue = []
        parent = {}
        queue.append(start)
        visited[start] = True

        while queue:
            current_node = queue.pop(0)

            if current_node == goal:
                # Goal node found, reconstruct the path
                path = [goal]
                while current_node != start:
                    current_node = parent[current_node]
                    path.insert(0, current_node)
                return path

            for neighbor in self.graph[current_node]:
                if neighbor <= max_vertex and not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    parent[neighbor] = current_node

if __name__ == '__main__':
    g = Graph()

    # Take input for the number of vertices and edges
    num_vertices = int(input("Enter the number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))

    # Take input for edges
    for _ in range(num_edges):
        u, v = map(int, input("Enter edge (u v): ").split())
        g.addEdge(u, v)

    # Take input for the starting and goal vertices
    start_vertex = int(input("Enter the starting vertex: "))
    goal_vertex = int(input("Enter the goal vertex: "))

    # Perform BFS to find the path to the goal node
    path_to_goal = g.BFS(start_vertex, goal_vertex)

    if path_to_goal:
        print(f"Path from {start_vertex} to {goal_vertex}: {path_to_goal}")
    else:
        print(f"No path found from {start_vertex} to {goal_vertex}")
      
Output:
Enter the number of vertices: 7
Enter the number of edges: 6
Enter edge (u v): 1 2
Enter edge (u v): 1 3
Enter edge (u v): 2 4
Enter edge (u v): 2 5
Enter edge (u v): 3 6
Enter edge (u v): 3 7
Enter the starting vertex: 1
Enter the goal vertex: 7
Path from 1 to 7: [1, 3, 7]


...Program finished with exit code 0
Press ENTER to exit console.
