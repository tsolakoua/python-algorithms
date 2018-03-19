graph = {}
graph["start"] = {}
graph["start"]["a"] = 3
graph["start"]["b"] = 5

graph["a"] = {}
graph["a"]["end"] = 2

graph["b"] = {}
graph["b"]["a"] = 6
graph["b"]["end"] = 4

graph["end"] = {}

costs = {}
costs["a"] = graph["start"]["a"]
costs["b"] = graph["start"]["b"]
costs["end"] = float("inf")

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["end"] = None

visited = []

def find_lowest_cost_node(costs):
	lowest_cost = float("inf")
	lowest_cost_node = None
	for node in costs:
		cost = costs[node]
		if cost < lowest_cost and node not in visited:
			lowest_cost_node = node
	return lowest_cost_node

def search_shortest_path():
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbour_nodes = graph[node]
        for i in neighbour_nodes.keys():
            new_cost = cost + neighbour_nodes[i]
            if costs[i] > new_cost:
                costs[i] = new_cost
                parents[i] = node
        visited.append(node)
        node = find_lowest_cost_node(costs)
        
search_shortest_path()
