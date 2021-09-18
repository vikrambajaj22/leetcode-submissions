def dfs_traversal(graph, start_node):
    '''
    :param graph: adjacency list
    :param start_node: node to start traversal from
    :return: DFS traversal
    '''
    visited = set()
    stack = [start_node]
    traversal = []

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            traversal.append(current)

            # add all neighbors of current to stack
            stack.extend(
                [node for node in graph[current] if node not in visited])

    return traversal


if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': [],
        'E': ['D']
    }
    print(dfs_traversal(graph, 'A'))
