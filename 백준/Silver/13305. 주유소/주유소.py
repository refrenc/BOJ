import sys

input = sys.stdin.readline

# 앞에 있는 도시 중 더 싼 동네로 갈 때까지만 충전
n = int(input())
roads = list(map(int, input().split()))
prices = list(map(int, input().split()))

distance = 0
price = prices[0]
result = 0
for i in range(1, n):
    distance += roads[i - 1]
    if price > prices[i]:
        # 정산
        result += distance * price
        distance = 0
        price = prices[i]
        continue


if distance != 0:
    result += distance * price

sys.stdout.write(str(result))

