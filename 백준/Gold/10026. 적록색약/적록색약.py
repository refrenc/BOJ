import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
color_print = []
cb_print = []
for _ in range(n):
    str = sys.stdin.readline().rstrip()
    color_print.append(list(str))
    cb_print.append(list(str))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
count_color = 0
for row in range(n):
    for col in range(len(color_print[row])):
        if color_print[row][col] == "":
            continue

        current = color_print[row][col]
        count_color += 1
        q = deque([])
        q.append((row, col))
        while q:
            y, x = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(color_print[row]) and 0 <= ny < n and color_print[ny][nx] == current:
                    q.append((ny, nx))
                    color_print[ny][nx] = ""

count_cb = 0
for row in range(n):
    for col in range(len(cb_print[row])):
        if cb_print[row][col] == "":
            continue

        current = cb_print[row][col]
        count_cb += 1
        q = deque([])
        q.append((row, col))
        cb_print[row][col] = ""
        while q:
            y, x = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(cb_print[row]) and 0 <= ny < n\
                    and (current == cb_print[ny][nx]\
                        or (current == "R" and cb_print[ny][nx] == "G")\
                        or (current == "G" and cb_print[ny][nx] == "R")):
                    q.append((ny, nx))
                    cb_print[ny][nx] = ""

print(count_color, count_cb)
