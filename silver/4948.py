# https://www.acmicpc.net/problem/4948
import sys
input = sys.stdin.readline


def sieve(n):
    m = n*2
    D = [True] * (m+1)
    D[0] = D[1] = False

    for i in range(0, m+1):
        if D[i]:
            for j in range(i*i, m+1, i):
                D[j] = False

    x = [i for i in range(n+1, m+1) if D[i]]

    return len(x)

result = []
while True:
    n = int(input())
    if n == 0:
        break
    result.append(sieve(n))

print("\n".join(map(str, result)))