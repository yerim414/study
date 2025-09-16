# https://www.acmicpc.net/problem/1259
result = []
while True:
    n = str(input())
    if n == "0":
        break

    result.append("yes" if n == n[::-1] else "no")

print(*result, sep='\n')