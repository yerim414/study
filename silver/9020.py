# https://www.acmicpc.net/problem/9020

def sieve(n):
    D = [True] * (n+1)
    D[0] = D[1] = False

    for i in range(2, int(n**0.5)+1):
        if D[i]:
            for j in range(i*i, n+1, i):
                D[j] = False

    return D

T = int(input())
prime_list = sieve(10000)
result = []

for _ in range(T):
    n = int(input())
    a, b = n//2, n//2
    while a >= 2:
        if prime_list[a] and prime_list[b]:
            result.append(f"{a} {b}")
            break
        a -= 1
        b += 1

print(*result, sep = "\n")