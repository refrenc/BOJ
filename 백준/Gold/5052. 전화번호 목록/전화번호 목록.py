import sys


def is_consistent(phones):
    for i in range(len(phones) - 1):
        if phones[i] == phones[i + 1][:len(phones[i])]:
            return False
    return True


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    phones = []
    for _ in range(n):
        phones.append(sys.stdin.readline().rstrip())
    phones.sort()

    if is_consistent(phones):
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")
