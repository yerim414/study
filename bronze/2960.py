# https://www.acmicpc.net/problem/2960

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

def sieve(n):
    x = [True]*(n+1)
    x[0] = x[1] = False
    count = 0
    for i in range(2, n+1):
        if x[i]:
            for j in range(i, n+1, i):
                if x[j]:
                    x[j] = False
                    count+=1
                    if count == K:
                        print(j)
                        exit()

sieve(N)