"""
         A
     /   |     \
    D    C      B
   /    /  \     \
  H     G   F     E
             \     \
              J     I

"""

graph = {
    "A": ["D", "C", "B"],
    "B": ["E"],
    "C": ["G", "F"],
    "D": ["H"],
    "E": ["I"],
    "F": ["J"],
}

# 深度優先搜尋法 Depth-first Search (DFS) - iterative
# ans: A B E I C F J G D H


def dfs_iterative(graph, source):

    if source is None or source not in graph:
        return "Invalid input"

    path = []
    stack = [source]

    while stack:
        s = stack.pop()

        if s not in path:
            path.append(s)

        if s not in graph:
            # leaf node
            continue

        for neighbor in graph[s]:
            stack.append(neighbor)

    return " ".join(path)


print(dfs_iterative(graph, "A"))
