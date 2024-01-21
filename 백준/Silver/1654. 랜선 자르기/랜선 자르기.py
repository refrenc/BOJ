import sys

input = sys.stdin.readline

k, n = list(map(int, input().split()))
lens = sorted([int(input()) for _ in range(k)])

# 랜선의 최대 길이로 이분탐색
lo = 1
hi = lens[-1]
while lo <= hi:
    mid = (lo + hi) // 2

    cnt = 0
    for len in lens:
        cnt += len // mid

    if cnt >= n:
        lo = mid + 1
    else:
        hi = mid - 1

sys.stdout.write(str(hi))
