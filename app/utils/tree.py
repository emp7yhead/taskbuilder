def get_dependencies(graph: dict, tasks: list[str]) -> list:
    visited = set()
    order = []

    def dfs_walk(node):
        visited.add(node)
        for successor in graph[node]:
            if successor not in visited:
                dfs_walk(successor)
        order.append(node)

    for task in get_unique(tasks):
        dfs_walk(task)
    return order


def get_unique(tasks: list[str]) -> list[str]:
    seen = set()
    return [
        task
        for task in tasks
        if task not in seen and not seen.add(task)  # type: ignore
    ]
