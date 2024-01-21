# 값이 계속 바뀌고 sort를 새로 해줘야하니 힙 사용
import heapq
import sys

result = 0
heap = []

n, m = sys.stdin.readline().rstrip().split()
nums = sys.stdin.readline().rstrip().split()

for num in nums:
    heapq.heappush(heap, int(num))

for _ in range(int(m)):
    min1, min2 = heapq.heappop(heap), heapq.heappop(heap)
    heapq.heappush(heap, min1 + min2)
    heapq.heappush(heap, min1 + min2)

sys.stdout.write(str(sum(heap)))
