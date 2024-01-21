def isVps(str):
    stack = []
    for s in str:
        if s == "(":
            stack.append(s)
            continue

        if len(stack) < 1:
            return False

        stack.pop()

    if (len(stack) > 0):
        return False

    return True

for i in range(int(input())):
    if(isVps(input())):
        print("YES")
    else:
        print("NO")

