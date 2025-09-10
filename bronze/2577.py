# https://www.acmicpc.net/problem/2577
import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

X = A*B*C

for i in range(0, 10):
    test = str(X).count(str(i))
    print(test)