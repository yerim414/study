# https://www.acmicpc.net/problem/2750
n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

a.sort()

for i in a:
    print(i) 

print(*a, sep="\n")