def bfs_traversal(graph, start_node):
    '''
    :param graph: adjacency list
    :param start_node: node to start traversal from
    :return: BFS traversal
    '''
    visited = set()
    queue = [start_node]
    traversal = []

    while queue:
        current = queue.pop(0)  # queue pops from front
        if current not in visited:
            visited.add(current)
            traversal.append(current)

            # add all neighbors of current to queue
            queue.extend(graph[current])

    return traversal


if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': [],
        'E': ['D']
    }
    print(bfs_traversal(graph, 'A'))
