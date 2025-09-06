a, b, c = map(int, input().split())

res1 = a * b // c
res2 = a * c // b

print(max(res1, res2))