import sys
from collections import deque

n, m, v = list(map(int, sys.stdin.readline().rstrip().split()))
edges = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = list(map(int, sys.stdin.readline().rstrip().split()))
    edges[v1].append(v2)
    edges[v2].append(v1)


def bfs(start):
    for edge in edges:
        edge.sort()

    visited = [start]
    q = deque([start])
    while q:
        node = q.popleft()
        for adj in edges[node]:
            if adj not in visited:
                q.append(adj)
                visited.append(adj)

    return visited


def dfs(start):
    for edge in edges:
        edge.sort(reverse=True)
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.append(node)
        for adj in edges[node]:
            if adj not in visited:
                stack.append(adj)

    return visited


if v != 0:
    print(" ".join(str(num) for num in dfs(v)))
    print(" ".join(str(num) for num in bfs(v)))
