import logging

from app.services.tasks import get_unique


def get_dependencies(graph: dict, tasks: list[str]) -> list:
    """
    Dependencies not in dict are 'white'
    Not finished dependencies marked as 'grey'
    Added dependencies is 'black'
    """
    visited = set()
    order = []

    def dfs_walk(node):
        logging.info(f'Get dependencies for "{node}" task')
        visited.add(node)
        for successor in graph[node]:
            if successor not in visited:
                dfs_walk(successor)
            else:
                logging.info(f'"{node}" already in dependecies')
        order.append(node)

    for task in get_unique(tasks):
        dfs_walk(task)
    return order
