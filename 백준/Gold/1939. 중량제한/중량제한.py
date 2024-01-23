import heapq
import sys

input = sys.stdin.readline


def is_safe(max_weight):
    # bfs
    q = []
    heapq.heappush(q, (0, factory1))
    visited = [False] * (n + 1)
    visited[factory1] = True
    while q:
        acc, cur = heapq.heappop(q)

        if cur == factory2:
            return True

        for adj, d in graph[cur]:
            if d >= max_weight and not visited[adj]:
                heapq.heappush(q, (d, adj))
                visited[adj] = True

    return False


n, m = list(map(int, input().split()))
graph = [[] for _ in range((n + 1))]
for _ in range(m):
    a, b, c = list(map(int, input().split()))
    graph[a].append((b, c))
    graph[b].append((a, c))
factory1, factory2 = list(map(int, input().split()))

# 중량 제한으로 이진탐색
lo = 0
hi = 2_000_000_000
result = 0
while lo < hi:
    mid = (lo + hi) // 2

    # 중량 제한보다 튼튼한 다리만 선택
    if not is_safe(mid):
        hi = mid
    else:
        result = mid
        lo = mid + 1

sys.stdout.write(str(result))
