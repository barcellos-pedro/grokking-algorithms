infinity = float('inf')

graph = {
    "start": {
        "a": 6,
        "b": 2
    },
    "a": {
        "end": 1
    },
    "b": {
        "a": 3,
        "end": 5
    },
    "end": {}
}


costs = {
    "a": 6,
    "b": 2,
    "end": infinity
}

parents = {
    "a": "start",
    "b": "start",
    "end": None
}

checked_nodes = []


def find_cheapest_node(costs):
    cheapest_node = None
    cheapest = infinity

    for key in costs:
        if key in checked_nodes:
            continue

        value = costs[key]

        if value < cheapest:
            cheapest = value
            cheapest_node = key

    return cheapest_node


def dijkstra(graph, costs, parents):
    # get closest(cheapest) node from the start
    node = find_cheapest_node(costs)

    # while has graphs to process
    while node is not None:
        neighbours = graph[node]
        node_cost = costs[node]

        for neighbour_key in neighbours.keys():
            # update node neighbours
            neighbour_cost = neighbours[neighbour_key]
            current_cost = node_cost + neighbour_cost

            # if its cheaper to go to its neighbour from current node, then update costs dict
            if costs[neighbour_key] > current_cost:
                # if neighbour cost value has been updated, then update its parent
                costs[neighbour_key] = current_cost
                parents[neighbour_key] = node

        # mark node as processed
        checked_nodes.append(node)
        node = find_cheapest_node(costs)

    # return path from start to end, following the parents dict
    return {"costs": costs, "parents": parents}


print(dijkstra(graph, costs, parents))
