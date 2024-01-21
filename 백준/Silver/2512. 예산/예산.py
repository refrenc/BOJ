import sys

input = sys.stdin.readline

n = int(input())
budget_reqs = sorted(list(map(int, input().split())))
budget_limit = int(input())

# 상한액 기준 이분탐색
lo = 1
hi = budget_reqs[-1]
result = 0
while lo <= hi:
    mid = (lo + hi) // 2

    # 상한액 mid 기준 합계 구하기
    sum = 0
    for budget_req in budget_reqs:
        sum += min(budget_req, mid)

    if budget_limit < sum:
        hi = mid - 1
    else:
        lo = mid + 1

sys.stdout.write(str(hi))
