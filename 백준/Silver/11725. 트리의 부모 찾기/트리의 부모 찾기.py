import sys
from collections import deque


n = int(sys.stdin.readline().rstrip())
edges = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    v1, v2 = list(map(int, sys.stdin.readline().rstrip().split()))
    edges[v1].append(v2)
    edges[v2].append(v1)

q = deque([1])
result = [0] * (n + 1)
while q:
    node = q.popleft()

    # 해당 노드의 인접한 노드에 대해
    for adj in edges[node]:
        # 이미 방문 > 부모 노드의 경우
        if result[adj] != 0:
            continue

        result[adj] = node
        q.append(adj)

for parent in result[2:]:
    sys.stdout.write(str(parent) + "\n")
