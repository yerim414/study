# https://www.acmicpc.net/problem/1181

n = int(input())

a = []
for i in range(n):
    a.append(input())

a = list(set(a))
a.sort()
a.sort(key=len)

print(*a, sep="\n")
# b= set(a)

# c = sorted(b)
# print(c)13