import sys

input = sys.stdin.readline

n, m = list(map(int, input().split()))
tree_heights = sorted(list(map(int, input().split())))

# 높이 기준 이진탐색
lo = 0
hi = tree_heights[-1]
result = 0
while lo <= hi:
    mid = (lo + hi) // 2

    sum = 0
    for tree in tree_heights:
        if tree > mid:
            sum += tree - mid

    if sum < m:
        hi = mid - 1
    else:
        lo = mid + 1

sys.stdout.write(str(hi))
