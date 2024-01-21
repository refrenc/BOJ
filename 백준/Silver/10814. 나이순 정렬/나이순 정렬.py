import sys

n = int(sys.stdin.readline().rstrip())
list = []
for i in range(n):
    age, name = sys.stdin.readline().rstrip().split()
    list.append((int(age), i, name))
list.sort()

sys.stdout.write("\n".join([' '.join((str(element[0]), element[2])) for element in list]))
