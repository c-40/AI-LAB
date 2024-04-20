from collections import deque

def bfs(graph, start, goal=None):
    visited = set()
    queue = deque([start])

    while queue:
        current = queue.popleft()
        if current == goal:
            print("Goal reached:", current)
            return
        if current not in visited:
            print(current, end=' ')
            visited.add(current)
            queue.extend(graph.get(current, []))

# Taking user input for the graph
graph = {}
num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    edge = input("Enter an edge (format: parent child): ").split()
    parent, child = edge
    if parent not in graph:
        graph[parent] = []
    graph[parent].append(child)

start_node = input("Enter the starting node: ")
goal_node = input("Enter the goal node: ")

print("BFS traversal:")
bfs(graph, start_node, goal_node)
