def aStarAlgo(start_node, stop_node, graph_nodes, heuristic_dist):
    open_set = set(start_node)
    closed_set = set()
    g = {}
    parents = {}
    g[start_node] = 0
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None

        for v in open_set:
            if n == None or g[v] + heuristic_dist[v] < g[n] + heuristic_dist[n]:
                n = v

        if n == stop_node or graph_nodes[n] == None:
            pass
        else:
            for (m, weight) in get_neighbors(n, graph_nodes):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        if n == None:
            print('Path does not exist!')
            return None

        if n == stop_node:
            path = []

            while parents[n] != n:
                path.append(n)
                n = parents[n]

            path.append(start_node)
            path.reverse()

            print('Path found: {}'.format(path))
            return path

        open_set.remove(n)
        closed_set.add(n)

    print('Path does not exist!')
    return None


def get_neighbors(v, graph_nodes):
    if v in graph_nodes:
        return graph_nodes[v]
    else:
        return None


def heuristic(n, heuristic_dist):
    return heuristic_dist[n]


# Get user input for graph and heuristic values
graph_nodes = {}
heuristic_dist = {}

num_nodes = int(input("Enter the number of nodes in the graph: "))
for _ in range(num_nodes):
    node = input("Enter the node: ")
    neighbors = input("Enter neighbors and their weights (comma-separated): ").split(',')
    neighbors = [(n.strip(), int(w.strip())) for n, w in map(lambda x: x.split(':'), neighbors)]
    graph_nodes[node] = neighbors

num_heuristics = int(input("Enter the number of heuristic values: "))
for _ in range(num_heuristics):
    node = input("Enter the node: ")
    value = int(input("Enter the heuristic value: "))
    heuristic_dist[node] = value

start_node = input("Enter the start node: ")
stop_node = input("Enter the stop node: ")

# Call the A* algorithm with user inputs
aStarAlgo(start_node, stop_node, graph_nodes, heuristic_dist)


# sample user input
# Enter the number of nodes in the graph: 10
# Enter the node: A
# Enter neighbors and their weights (comma-separated): B:6, F:3
# Enter the node: B
# Enter neighbors and their weights (comma-separated): C:3, D:2
# Enter the node: C
# Enter neighbors and their weights (comma-separated): D:1, E:5
# Enter the node: D
# Enter neighbors and their weights (comma-separated): C:1, E:8
# Enter the node: E
# Enter neighbors and their weights (comma-separated): I:5, J:5
# Enter the node: F
# Enter neighbors and their weights (comma-separated): G:1, H:7
# Enter the node: G
# Enter neighbors and their weights (comma-separated): I:3
# Enter the node: H
# Enter neighbors and their weights (comma-separated): I:2
# Enter the node: I
# Enter neighbors and their weights (comma-separated): E:5, J:3
# Enter the node: J
# Enter neighbors and their weights (comma-separated): 

# Enter the number of heuristic values: 10
# Enter the node: A
# Enter the heuristic value: 10
# Enter the node: B
# Enter the heuristic value: 8
# Enter the node: C
# Enter the heuristic value: 5
# Enter the node: D
# Enter the heuristic value: 7
# Enter the node: E
# Enter the heuristic value: 3
# Enter the node: F
# Enter the heuristic value: 6
# Enter the node: G
# Enter the heuristic value: 5
# Enter the node: H
# Enter the heuristic value: 3
# Enter the node: I
# Enter the heuristic value: 1
# Enter the node: J
# Enter the heuristic value: 0

# Enter the start node: A
# Enter the stop node: J
