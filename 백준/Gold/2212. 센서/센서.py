import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
position = list(map(int, input().split()))
position.sort()

if n <= k:
    sys.stdout.write("0")
else:
    # 집중국 사이의 거리를 내림차순으로 정렬 후 n-1개의 거리를 뺌
    distance = [position[i + 1] - position[i] for i in range(len(position) - 1)]
    distance.sort(reverse=True)
    result = sum(distance)
    for i in range(k - 1):
        result -= distance[i]

    sys.stdout.write(str(result))
