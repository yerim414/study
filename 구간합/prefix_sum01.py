# https://www.acmicpc.net/problem/11659

num, quiz = map(int, input().split())
a = list(map(int, input().split()))

temp = 0
prefix_sum = [0]

for i in a:
    temp += i
    prefix_sum.append(temp)
5 

for i in range(quiz):
    x, y = map(int, input().split())

    result = prefix_sum[y] - prefix_sum[x-1]
    print(result)