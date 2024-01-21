import sys


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    parent[max(a, b)] = min(a, b)


n, m = list(map(int, sys.stdin.readline().rstrip().split()))
edges = []
for _ in range(m):
    a, b, c = list(map(int, sys.stdin.readline().rstrip().split()))
    edges.append((c, a, b))
edges.sort()

parent = [i for i in range(n + 1)]
result = 0
maxCost = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        maxCost = max(maxCost, cost)

sys.stdout.write(str(result - maxCost))
