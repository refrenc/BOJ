import sys
input = sys.stdin.readline

n = int(input())
list = []
for _ in range(n):
    list.append(int(input()))

list.sort()
sys.stdout.write("\n".join(map(str, list)))
