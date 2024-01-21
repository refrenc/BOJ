# 선입선출 보장되어야 함 > 큐
import sys
from collections import deque, defaultdict

result = 0
inQueue = deque([])
outQueue = deque([])
overtake = defaultdict(bool)

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    inQueue.append(sys.stdin.readline().rstrip())
for _ in range(n):
    outQueue.append(sys.stdin.readline().rstrip())

while inQueue:
    if overtake[inQueue[0]]:
        inQueue.popleft()
    elif inQueue[0] == outQueue[0]:
        inQueue.popleft()
        outQueue.popleft()
    else:
        overtake[outQueue.popleft()] = True

sys.stdout.write(str(sum(value for value in overtake.values() if value)))
