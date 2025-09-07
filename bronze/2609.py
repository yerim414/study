# https://www.acmicpc.net/problem/2609

# 유클리드 호제
n, m = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(n,m))
print(n*m // gcd(n, m))

# math 모듈 사용
import math

n, m = map(int, input().split())
print(math.gcd(n,m))
print(math.lcm(n,m))