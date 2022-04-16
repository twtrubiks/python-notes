"""
         A
     /   |     \
    B    C      D
   /    /  \     \
  E     F   G     H
 /     /     
I      J

"""

graph = {
    "A": ["B", "C", "D"],
    "B": ["E"],
    "C": ["F", "G"],
    "D": ["H"],
    "E": ["I"],
    "F": ["J"],
}

# 深度優先搜尋法 Depth-first Search (DFS) - recursive
# ans: ['A', 'B', 'E', 'I', 'C', 'F', 'J', 'G', 'D', 'H']


def recursive_dfs(graph, source, path=[]):

    if source not in path:
        path.append(source)

        if source not in graph:
            # leaf node, backtrack
            return path

        for neighbour in graph[source]:
            path = recursive_dfs(graph, neighbour, path)

    return path


print(" ".join(recursive_dfs(graph, "A")))
