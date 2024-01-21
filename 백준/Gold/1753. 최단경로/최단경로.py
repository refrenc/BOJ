import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

v, e = list(map(int, input().split()))
k = int(input())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    start, end, w = list(map(int, input().split()))
    graph[start].append((end, w))

q = []
dist = [INF] * (v + 1)
heapq.heappush(q, (0, k))
dist[k] = 0
while q:
    acc, cur = heapq.heappop(q)

    if dist[cur] < acc:
        continue

    for adj, d in graph[cur]:
        cost = d + acc
        if cost < dist[adj]:
            dist[adj] = cost
            heapq.heappush(q, (cost, adj))

for d in dist[1:]:
    sys.stdout.write(str(d if d < INF else "INF") + "\n")
