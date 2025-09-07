# https://www.acmicpc.net/problem/15726
N, X = map(int,input().split())

A = list(map(int,input().split()))

count = []

for idx in range(N-1):
    count.append((A[idx] * X) + (A[idx+1] * X))

print(min(count))