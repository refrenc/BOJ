import sys


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    parent[max(a, b)] = min(a, b)


n = int(sys.stdin.readline().rstrip())
edges = []
for i in range(n):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(n):
        if i < j:
            edges.append((row[j], i, j))
edges.sort()

result = 0
parents = [i for i in range(n + 1)]
for edge in edges:
    cost, i, j = edge
    if find_parent(parents, i) != find_parent(parents, j):
        union_parent(parents, i, j)
        result += cost

print(result)
