# https://www.acmicpc.net/problem/11660

size, quiz = map(int, input().split())

# 첫번째 줄 index 0 값은 0으로 초기화 한다.
# 1 base 기준으로 작성할것이기 때문
a = [[0] * (size + 1)] # 원본
s = [[0] * (size + 1)] # 합 배열

for i in range(size):
    data = [0] + list(map(int, input().split()))
    a.append(data)

# 합배열 생성
for i in range(1, size+1):
    for j in range(1, size+1):
        s[i][j] = s[i][j-1] + s[i-1][j] - s[i-1][j-1] + a[i][j]

for _ in range(quiz):
    x1, y1, x2, y2 = map(int, input().split())
    print(s[x2][y2] - s[x1-1][y2] - s[x2][y1-1] + s[x1-1][y1-1])
