import sys
from collections import deque

arr = [1, 2, 3]
def bfs(target):
    result = []
    q = deque([[]])

    while q:
        node = q.popleft()
        if sum(node) == target:
            result.append(node[:])
            continue
        for i in range(len(arr)):
            if sum(node) + arr[i] <= target:
                q.append(node + [arr[i]])

    return result


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    sys.stdout.write(str(len(bfs(n))) + "\n")
