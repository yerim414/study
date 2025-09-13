# https://www.acmicpc.net/problem/2960

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

D = [True for _ in range(N+1)]
D[0] = D[1] = False
count = 0

for i in range(2, N+1):
    if D[i]:
        for j in range(i, N+1, i):
            D[j] = False
            count +1
            if count == K:
                print(j)
                exit()