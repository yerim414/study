import sys
input = sys.stdin.readline

n = int(input())
A = set(map(int,input().split()))

M = int(input())
B = list(map(int,input().split()))

for i in B:
    print(1 if i in A else 0)