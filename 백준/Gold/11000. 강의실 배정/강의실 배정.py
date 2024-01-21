import heapq
import sys

n = int(sys.stdin.readline().rstrip())
lectures = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
lectures.sort()

classrooms = [lectures[0][1]]
for lecture in lectures[1:]:
    # 새로 넣을 수업의 시작하는 시간(lecture[0])이 가장 빨리 끝나는 강의실의 시간보다 후에 있어야 교체
    if classrooms[0] <= lecture[0]:
        heapq.heappop(classrooms)

    heapq.heappush(classrooms, lecture[1])

sys.stdout.write(str(len(classrooms)))
