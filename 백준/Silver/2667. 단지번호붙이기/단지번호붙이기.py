import sys

n = int(sys.stdin.readline().rstrip())

# 맵 만들기
map = []
for _ in range(n):
    input = sys.stdin.readline().rstrip()
    temp = []
    for char in input:
        temp.append(int(char))
    map.append(temp)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
rows, cols = len(map), len(map[0])
result = []

for row in range(rows):
    for col in range(cols):
        if map[row][col] != 1:
            continue

        houseNum = 0
        stack = [(row, col)]

        while stack:
            x, y = stack.pop()
            if map[x][y] == 1:
                houseNum += 1
            map[x][y] = 0
            # 4방향 검사
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= rows or ny < 0 or ny >= cols or map[nx][ny] != 1:
                    continue
                stack.append((nx, ny))
        result.append(houseNum)

result.sort()
sys.stdout.write(str(len(result)) + "\n")
for count in result:
    sys.stdout.write(str(count) + "\n")
