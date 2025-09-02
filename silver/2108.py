# https://www.acmicpc.net/problem/2108

from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())

a = []
for _ in range(n):
    a.append(int(input()))

# # 산술평균
# sum_ = sum(a) / n
# print(round(sum_))

# # 중앙값
# b = sorted(a)
# x = (n//2)
# print(b[x])

# 최빈값
counter = Counter(a)
freq = counter.most_common()
max_count = freq[0][1]
modes = [num for num, count in freq if count == max_count]
if len(modes) > 1:
    modes.sort()
    print(modes[1])
else:
    print(modes[0])

# # 범위
# max_ = max(a)
# min_ = min(a)
# print(max_- min_)