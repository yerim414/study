# https://www.acmicpc.net/problem/2851
N = [int(input()) for _ in range(10)]

total = 0
result = 0
for i in N:
    total += i
    if abs(100 - total) <= abs(100 - result):
        result = total

print(result)