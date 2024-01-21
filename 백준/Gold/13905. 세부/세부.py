import sys

sys.setrecursionlimit(10 ** 5)


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    parent[max(a, b)] = min(a, b)


n, m = list(map(int, sys.stdin.readline().rstrip().split()))
s, e = list(map(int, sys.stdin.readline().rstrip().split()))

edges = []
for _ in range(m):
    h1, h2, k = list(map(int, sys.stdin.readline().rstrip().split()))
    edges.append((k, h1, h2))
edges.sort()

parent = [i for i in range(n + 1)]
result = 0
while find_parent(parent, s) != find_parent(parent, e) and edges:
    cost, h1, h2 = edges.pop()
    result = cost
    union_parent(parent, h1, h2)

sys.stdout.write(str(result if find_parent(parent, s) == find_parent(parent, e) else 0))
