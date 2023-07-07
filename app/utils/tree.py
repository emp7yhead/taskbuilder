import logging

from fastapi import HTTPException

from app.services.tasks import get_unique


def get_dependencies(graph: dict, tasks: list[str]):
    """
    Dependencies not in dict are 'white'
    Not finished dependencies marked as 'grey'
    Added dependencies is 'black'
    """
    color = dict()
    order = []

    def dfs_walk(node):
        logging.info(f'Get dependencies for "{node}" task')
        color[node] = 'grey'
        for successor in graph[node]:
            if color.get(successor) == 'grey':
                raise HTTPException(
                    422, f'Circular dependencies found in {successor}'
                )
            if successor not in color:
                dfs_walk(successor)
            else:
                logging.info(f'"{node}" already in dependecies')
        order.append(node)
        color[node] = 'black'

    for task in get_unique(tasks):
        dfs_walk(task)
    return order
