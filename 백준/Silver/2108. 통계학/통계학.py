import sys

n = int(sys.stdin.readline().rstrip())
nums = []
sum = 0
max_num = -4000
min_num = 4000
freq = {}
max_freq = 0
max_freq_nums = []
for _ in range(n):
    input = int(sys.stdin.readline().rstrip())
    nums.append(input)

    sum += input
    max_num = max(max_num, input)
    min_num = min(min_num, input)
    if input not in freq:
        freq[input] = 1
    else:
        freq[input] += 1
    if max_freq < freq[input]:
        max_freq_nums = [input]
    elif max_freq == freq[input]:
        max_freq_nums.append(input)
    max_freq = max(max_freq, freq[input])
nums.sort()

# 산술평균
sys.stdout.write(str(round(sum / n)) + "\n")
# 중앙값
sys.stdout.write(str(nums[n // 2]) + "\n")
# 최빈값
max_freq_num = 0
if len(max_freq_nums) < 2:
    max_freq_num = max_freq_nums[0]
else:
    max_freq_nums.sort()
    max_freq_num = max_freq_nums[1]
sys.stdout.write(str(max_freq_num) + "\n")
# 범위
sys.stdout.write(str(max_num - min_num) + "\n")
