import heapq
import sys

n = int(sys.stdin.readline().rstrip())
heap = []

for _ in range(n):
    input = int(sys.stdin.readline().rstrip())
    if input == 0:
        if len(heap) < 1:
            sys.stdout.write("0")
        else:
            sys.stdout.write(str(heapq.heappop(heap)))
        sys.stdout.write("\n")
        continue
    heapq.heappush(heap, input)