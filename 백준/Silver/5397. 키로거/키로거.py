import sys

class ListNode:
    def __init__(self, val="", prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

    def toPrev(self):
        if not self.prev:
            return self
        return self.prev

    def toNext(self):
        if not self.next:
            return self
        return self.next

    def delete(self):
        if not self.prev:
            return self

        prev, next = self.prev, self.next
        if prev:
            prev.next = next
        if next:
            next.prev = prev

        return prev

    def add(self, val):
        next = self.next
        self.next = ListNode(val, self, next)
        if next:
            next.prev = self.next
        return self.next


n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    head = ListNode()
    current = head
    input = sys.stdin.readline().rstrip()
    for char in input:
        if char == "<":
            current = current.toPrev()
        elif char == ">":
            current = current.toNext()
        elif char == "-":
            current = current.delete()
        else:
            current = current.add(char)

    # current를 head로
    while current.prev:
        current = current.prev

    # 출력
    while True:
        sys.stdout.write(current.val)
        current = current.next
        if not current:
            sys.stdout.write("\n")
            break
