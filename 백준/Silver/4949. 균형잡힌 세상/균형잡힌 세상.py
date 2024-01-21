import sys

pair = {")": "(", "]": "["}

while True:
    input = sys.stdin.readline().rstrip()
    if input == ".":
        break

    stack = []
    for char in input:
        # (, [은 stack에 넣음
        if char in pair.values():
            stack.append(char)
            continue

        # ), ]은 stack pop과 비교
        if char in pair.keys():
            if not stack or stack.pop() != pair[char]:
                sys.stdout.write("no\n")
                break

        # .이면 끝
        if char == ".":
            if not stack:
                sys.stdout.write("yes\n")
                break
            else:
                sys.stdout.write("no\n")
                break
