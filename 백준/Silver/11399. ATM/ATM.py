import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()

result = 0
for i in range(n):
    result += sum(lst[:i + 1])

sys.stdout.write(str(result))
