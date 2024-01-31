Input:
def dfs(tree, current, visited=None, goal=None):
    if visited is None:
        visited = set()

    visited.add(current)
    print(current, end=' ')

    if goal is not None and current == goal:
        print("\nGoal vertex reached!")
        return

    for child in tree.get(current, []):
        if child not in visited:
            dfs(tree, child, visited, goal)

# Take input for the tree
tree = {}
num_nodes = int(input("Enter the number of nodes in the tree: "))

for _ in range(num_nodes - 1):
    edge = input("Enter edge (format: parent child): ").split()
    parent, child = edge
    if parent not in tree:
        tree[parent] = []
    tree[parent].append(child)

# Take input for the starting node
start_node = input("Enter the starting node: ")

# Take input for the goal node
goal_node = input("Enter the goal node (or leave blank for regular DFS): ")

# Perform DFS on the tree
print("Depth-First Search:")
dfs(tree, start_node, goal=goal_node if goal_node else None)

Output:
Enter the number of nodes in the tree: 7 
Enter edge (format: parent child): 9 7
Enter edge (format: parent child): 9 3
Enter edge (format: parent child): 7 5
Enter edge (format: parent child): 7 1
Enter edge (format: parent child): 3 2
Enter edge (format: parent child): 3 4
Enter the starting node: 9
Enter the goal node (or leave blank for regular DFS): 1
Depth-First Search:
9 7 5 1 
Goal vertex reached!
