import sys
from collections import deque


def bfs():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    result = []
    q = deque([(0, start_y, start_x)])
    visited = [[False] * n for _ in range(n)]
    visited[start_y][start_x] = True
    while q:
        len, y, x = q.popleft()
        if graph[y][x] > 0 and graph[y][x] < bs_weight:
            result.append((len, y, x))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[ny][nx] > bs_weight or visited[ny][nx]:
                continue
            q.append((len + 1, ny, nx))
            visited[ny][nx] = True

    # 정렬
    return result


n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n)]
start_y, start_x = 0, 0
for i in range(n):
    graph[i] = list(map(int, sys.stdin.readline().rstrip().split()))
    if 9 in graph[i]:
        start_y = i
        start_x = graph[i].index(9)
        graph[start_y][start_x] = 0

eat_num = 0
bs_weight = 2
time = 0
while True:
    next = bfs()
    if not next:
        break

    next.sort()
    len, ny, nx = next[0]

    # 무게 계산
    eat_num += 1
    if eat_num == bs_weight:
        bs_weight += 1
        eat_num = 0

    graph[ny][nx] = 0
    time += len
    start_y, start_x = ny, nx

print(time)
