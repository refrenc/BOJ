import sys
from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    l = int(sys.stdin.readline().rstrip())
    current = tuple(map(int, sys.stdin.readline().rstrip().split()))
    target = tuple(map(int, sys.stdin.readline().rstrip().split()))

    # 최단 거리니까 bfs
    visited = [[False] * l for _ in range(l)]
    q = deque([(0, current[0], current[1])])
    visited[current[0]][current[1]] = True
    while q:
        count, y, x = q.popleft()
        if y == target[0] and x == target[1]:
            sys.stdout.write(str(count) + "\n")
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and not visited[ny][nx]:
                q.append((count + 1, ny, nx))
                visited[ny][nx] = True
