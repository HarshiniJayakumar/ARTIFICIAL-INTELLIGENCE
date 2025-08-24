import heapq
def greedy_best_first_search(graph, start, goal, heuristic):
    priority_queue = [(heuristic[start], start, [start])]
    visited = set()
    while priority_queue:
        current_heuristic_cost, current_node, path = heapq.heappop(priority_queue)
        if current_node in visited:
            continue
        visited.add(current_node)
        if current_node == goal:
            return path
        for neighbor, cost in graph.get(current_node, {}).items():
            if neighbor not in visited:
                new_path = path + [neighbor]
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor, new_path))
    return None  
if __name__ == "__main__":
    graph1 = {
    'A': {'B': 1, 'C': 5},
    'B': {'D': 3, 'E': 6},
    'C': {'F': 2},
    'D': {'G': 4},
    'E': {'G': 2},
    'F': {'G': 7},
    'G': {}
    }
    heuristic1 = {
    'A': 7, 'B': 2, 'C': 6,
    'D': 1, 'E': 4, 'F': 5,
    'G': 0
    }
    start_node = 'A'
    goal_node = 'G'
    path_found = greedy_best_first_search(graph1, start_node, goal_node, heuristic1)
    if path_found:
        print(f"Path from {start_node} to {goal_node}: {path_found}")
    else:
        print(f"No path found from {start_node} to {goal_node}")
    graph2 = {
    'S': {'A': 1, 'B': 5},
    'A': {'C': 2, 'D': 3},
    'B': {'E': 4},
    'C': {'G': 6},
    'D': {'G': 2},
    'E': {'G': 1}
    }
    heuristic2 = {
    'S': 7, 'A': 2, 'B': 6,
    'C': 4, 'D': 1, 'E': 5,
    'G': 0
    }
    start_node2 = 'S'
    goal_node2 = 'G'

    path_found2 = greedy_best_first_search(graph2, start_node2, goal_node2, heuristic2)

    if path_found2:
        print(f"Path from {start_node2} to {goal_node2}: {path_found2}")
    else:
        print(f"No path found from {start_node2} to {goal_node2}")