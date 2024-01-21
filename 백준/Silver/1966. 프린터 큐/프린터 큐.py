from collections import deque

def getPrintOrder(priorities, target):
    queue = deque(enumerate(priorities))
    result = 0

    while True:
        current = queue.popleft()
        if any(current[1] < doc[1] for doc in queue):
            queue.append(current)
            continue

        result += 1;
        if(current[0] == target):
            return result

testNum = int(input())

for test in range(testNum):
    docNum, targetNum = map(int, input().split())
    priorities = list(map(int, input().split()))

    print(getPrintOrder(priorities, targetNum))