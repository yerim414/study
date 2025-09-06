# https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())

A = []
for _ in range(n):
    A.append(int(input()))

A.sort(reverse=True)

sum = 0
for i in A:
    if k == 0:
        break
    if i <= k:
        sum = sum + (k//i)
        k = k % i

print(sum)