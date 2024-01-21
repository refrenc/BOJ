n = int(input())
strs = dict.fromkeys(input().split(), True)
m = int(input())
inputStrs = input().split()
for i in range(m):
    if inputStrs[i] in strs:
        print("1")
        continue
    print("0")