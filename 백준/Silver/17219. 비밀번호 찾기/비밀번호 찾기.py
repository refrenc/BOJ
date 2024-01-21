addressNum, findNum = map(int, input().split())

addressSet = {}
for i in range(addressNum):
    address, password = input().split()
    addressSet[address] = password

for i in range(findNum):
    print(addressSet[input()])