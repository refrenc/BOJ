import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, x = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
dist = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    start, end, time = list(map(int, input().split()))
    graph[start].append((end, time))

for i in range(1, n + 1):
    q = []
    heapq.heappush(q, (0, i))
    dist[i][i] = 0
    while q:
        acc, cur = heapq.heappop(q)

        if dist[i][cur] < acc:
            continue

        for adj, d in graph[cur]:
            cost = d + acc
            if cost < dist[i][adj]:
                dist[i][adj] = cost
                heapq.heappush(q, (cost, adj))

result = 0
for a in range(1, n + 1):
    result = max(result, dist[a][x] + dist[x][a])

sys.stdout.write(str(result))
