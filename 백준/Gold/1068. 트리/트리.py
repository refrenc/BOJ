import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
parents = list(map(int, sys.stdin.readline().rstrip().split()))
delete = int(sys.stdin.readline().rstrip())

edges = [[] for _ in range(n)]
for i in range(len(parents)):
    if parents[i] == -1:
        continue
    if i != delete:
        edges[parents[i]].append(i)

# 삭제
q = deque([delete])
while q:
    node = q.popleft()

    for adj in edges[node]:
        q.append(adj)

    edges[node] = [node]

print(edges.count([]))
