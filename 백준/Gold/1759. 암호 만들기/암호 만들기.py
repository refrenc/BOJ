import sys
from collections import deque

"""
암호 조건
    1. 서로 다른 l개의 알파벳 소문자
    2. 최소 한 개의 모음 len([dup for dup in node if dup in vowels])
    3. 최소 두 개의 자음 len([dup for dup in node if dup not in vowels])
    4. 오름차순 정렬
"""
MIN_VOWEL_NUM = 1
MIN_CONSO_NUM = 2


l, c = list(map(int, sys.stdin.readline().rstrip().split()))

vowels = ["a", "e", "i", "o", "u"]

chance = sys.stdin.readline().rstrip().split()
chance.sort()

result = []
q = deque([([], -1)])
while q:
    node, index = q.popleft()
    vowelNum = len([dup for dup in node if dup in vowels])
    if len(node) == l:
        if vowelNum >= MIN_VOWEL_NUM \
                and (len(node) - vowelNum) >= MIN_CONSO_NUM:
            result.append(node[:])
        continue

    for i in range(index + 1, len(chance)):
        if chance[i] not in node:
            q.append((node + [chance[i]], i))

print("\n".join("".join(string for string in row) for row in result))
