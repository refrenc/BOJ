import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    lst = [tuple(map(int, input().split())) for _ in range(n)]
    lst.sort()

    select = [lst[0]]
    for i in range(1, n):
        if select[-1][0] < lst[i][0] and select[-1][1] < lst[i][1]:
            continue
        select.append(lst[i])

    sys.stdout.write(str(len(select)) + "\n")
