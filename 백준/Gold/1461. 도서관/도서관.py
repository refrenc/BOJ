import sys

input = sys.stdin.readline

n, m = list(map(int, input().split()))
positions = list(map(int, input().split()))
position_neg = []
position_pos = []
for position in positions:
    if position < 0:
        position_neg.append(position)
    else:
        position_pos.append(position)
position_neg.sort()
position_pos.sort(reverse=True)

result = 0
# 절대값이 큰 수부터 더함, 마지막에 가장 큰 절대값 뺌
# 음수
book_num = 0
temp_book = position_neg[0] if position_neg else 0
for neg in position_neg:
    if book_num == m:
        result += 2 * abs(temp_book)
        book_num = 0
        temp_book = neg
    book_num += 1
result += 2 * abs(temp_book)

book_num = 0
temp_book = position_pos[0] if position_pos else 0
for neg in position_pos:
    if book_num == m:
        result += 2 * abs(temp_book)
        book_num = 0
        temp_book = neg
    book_num += 1
result += 2 * abs(temp_book)

sys.stdout.write(str(result - max(abs(min(positions)), abs(max(positions)))))
