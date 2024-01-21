import sys


# kruskal
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    parent[max(a, b)] = min(a, b)


n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
edges = []
for _ in range(m):
    a, b, cost = tuple(map(int, sys.stdin.readline().rstrip().split()))
    edges.append((cost, a, b))
edges.sort()

result = 0
parent = [i for i in range(n + 1)]
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

sys.stdout.write(str(result))
