import sys

input = sys.stdin.readline

n = int(input())

"""
1. 1번 집 != 2번 집
2. n번 집 != n-1번 집
3. i번 집 != i-1번 집 && i번 집 != i+1번 집
"""

dp = [[0] * 3 for _ in range(n)]
costs = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    dp[i][0] = costs[i][0] + min(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = costs[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = costs[i][2] + min(dp[i - 1][0], dp[i - 1][1])

sys.stdout.write(str(min(dp[-1])))
