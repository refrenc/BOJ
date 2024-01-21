import sys


def spread(graph):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    graph_diff = [[0] * c for _ in range(r)]
    for row in range(len(graph)):
        for col in range(len(graph[row])):
            if graph[row][col] < 1:
                continue

            spread_amount = graph[row][col] // 5
            spread_num = 0
            for i in range(4):
                x, y = col + dx[i], row + dy[i]
                if x > -1 and x < c and y > -1 and y < r and graph[y][x] != -1:
                    graph_diff[y][x] += spread_amount
                    spread_num += 1
            graph[row][col] -= spread_amount * spread_num

    for row in range(len(graph)):
        for col in range(len(graph[row])):
            graph[row][col] += graph_diff[row][col]


def clean(graph, air_cleaner_upper):
    clockwise = [[(1, 0), (0, -1), (-1, 0), (0, 1)],
                 [(1, 0), (0, 1), (-1, 0), (0, -1)]]
    air_cleaner = [(0, air_cleaner_upper), (0, air_cleaner_upper + 1)]
    for i in range(2):
        direction = 0
        x, y = air_cleaner[i]
        prev = 0
        while True:
            x += clockwise[i][direction][0]
            y += clockwise[i][direction][1]
            if x > -1 and x < c and y > -1 and y < r:
                if graph[y][x] == -1:
                    break
                graph[y][x], prev = prev, graph[y][x]

                # 방향 전환
                temp_x, temp_y = x + clockwise[i][direction][0], y + clockwise[i][direction][1]
                if temp_x < 0 or temp_x >= c or temp_y < 0 or temp_y >= r:
                    direction += 1


r, c, t = list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(r)]
air_cleaner = 0
for i in range(r):
    graph[i] = list(map(int, sys.stdin.readline().split()))
    if graph[i][0] == -1 and air_cleaner == 0:
        air_cleaner = i

# t초 동안 확산, 이동
for _ in range(t):
    spread(graph)
    clean(graph, air_cleaner)

total_sum = sum(element for row in graph for element in row)
sys.stdout.write(str(total_sum + 2))
