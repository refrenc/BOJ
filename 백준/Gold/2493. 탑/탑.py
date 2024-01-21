import sys

n = int(sys.stdin.readline().rstrip())
result = [0] * n

heights = list(map(int, sys.stdin.readline().rstrip().split()))
stack = []

for i in range(n - 1, -1, -1):
    if not stack:
        stack.append(i)
        continue

    if heights[stack[-1]] < heights[i]:
        while stack and heights[stack[-1]] < heights[i]:
            index = stack.pop()
            result[index] = i + 1

    stack.append(i)

print(" ".join(map(str, result)))
