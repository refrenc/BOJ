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
total = 0
for i in range(n):
    row = list(sys.stdin.readline().rstrip())
    for j in range(n):
        if row[j] == "0":
            continue

        ch = ord(row[j])
        cost = 0
        if 'a' <= row[j] <= 'z':
            cost = ch - ord('a') + 1
        else:
            cost = ch - ord('A') + 27
        total += cost
        edges.append((cost, i, j))
edges.sort()

result = []
parents = [i for i in range(n)]
sum = 0
for edge in edges:
    cost, i, j = edge
    if find_parent(parents, i) != find_parent(parents, j):
        union_parent(parents, i, j)
        sum += cost

root_set = set(find_parent(parents, i) for i in range(n))
if len(root_set) > 1:
    print(-1)
else:
    print(total - sum)
