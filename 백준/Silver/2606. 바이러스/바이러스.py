import sys

stack = []

computerNum = int(sys.stdin.readline().rstrip())
edgeNum = int(sys.stdin.readline().rstrip())

edges = []
for _ in range(edgeNum):
    edges.append(tuple(map(int, sys.stdin.readline().rstrip().split())))

# 1번 컴퓨터가 존재 할 때만 stack에 append
for edge in edges:
    if edge[0] == 1:
        stack.append(edge)

# dfs
visited = [False] * (computerNum + 1)
while stack:
    start, end = stack.pop()
    visited[start] = True
    visited[end] = True
    # end가 시작점인 edge들 stack에 append
    for edge in edges:
        if (edge[0] == end or edge[1] == end or edge[0] == start or edge[1] == start) and not (visited[edge[1]] and visited[edge[0]]):
            stack.append(edge)

count = visited.count(True) - 1
if count < 1:
    count = 0
sys.stdout.write(str(count))
