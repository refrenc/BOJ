import copy
import sys


def is_available(sticker, y, x):
    for row in range(len(sticker)):
        for col in range(len(sticker[row])):
            if sticker[row][col] == 0:
                continue

            if x + col >= m or y + row >= n or computer[y + row][x + col] == 1:
                return False

    return True


def find(sticker):
    for row in range(n):
        for col in range(m):
            if is_available(sticker, row, col):
                return (row, col)
    return None


def paste(sticker, y, x):
    height, width = len(sticker), len(sticker[0])
    for i in range(height):
        for j in range(width):
            if sticker[i][j] == 0:
                continue
            computer[y + i][x + j] = sticker[i][j]


def rotate_90(sticker):
    height, width = len(sticker), len(sticker[0])
    new_sticker = [[0] * height for _ in range(width)]
    for row in range(height):
        for col in range(width):
            new_sticker[col][row] = sticker[height - row - 1][col]

    return new_sticker



n, m, k = list(map(int, sys.stdin.readline().rstrip().split()))
computer = [[0] * m for _ in range(n)]
stickers = []
for _ in range(k):
    r, c = list(map(int, sys.stdin.readline().rstrip().split()))
    sticker = []
    for _ in range(r):
        sticker.append(list(map(int, sys.stdin.readline().rstrip().split())))
    stickers.append(sticker)

for sticker in stickers:
    """
    1. 스티커를 붙일 위치 찾기
    2. 붙인다.
        2-1. 못붙였다면 시계 방향으로 회전 후 2번
        2-2. 4방향 다 안되면 버림
    """
    current = copy.deepcopy(sticker)
    for _ in range(4):
        position = find(current)
        if not position:
            current = rotate_90(current)
            continue

        paste(current, position[0], position[1])
        break


print(sum(element == 1 for row in computer for element in row))
