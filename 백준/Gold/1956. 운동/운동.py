import sys

input = sys.stdin.readline

INF = int(1e9)

v, e = list(map(int, input().split()))
dist = [[INF] * (v + 1) for _ in range(v + 1)]
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = list(map(int, input().split()))
    graph[a].append((b, c))
    dist[a][b] = c

for idx in range(1, v + 1):
    dist[idx][idx] = 0

for k in range(1, v + 1):
    for a in range(1, v + 1):
        for b in range(1, v + 1):
            dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

result = INF
for a in range(1, v + 1):
    for b in range(1, v + 1):
        if a == b or a < b:
            continue
        result = min(result, dist[a][b] + dist[b][a])
sys.stdout.write(str(result if result < INF else -1))
