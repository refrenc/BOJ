import heapq
import sys

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

problem_num = 1
while True:
    n = int(input())
    if n < 1:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]

    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    visited = [[False] * n for _ in range(n)]
    while q:
        dist, y, x = heapq.heappop(q)
        if y == n - 1 and x == n - 1:
            sys.stdout.write("Problem " + str(problem_num) + ": " + str(dist) + "\n")
            problem_num += 1
            break

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                heapq.heappush(q, (dist + graph[ny][nx], ny, nx))
                visited[ny][nx] = True
