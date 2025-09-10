# https://www.acmicpc.net/problem/11966
n = int(input())

print(1 if n > 0 and (n & (n - 1)) == 0 else 0)