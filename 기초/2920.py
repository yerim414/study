# https://www.acmicpc.net/problem/2920

a = list(map(int, input().split()))

ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = [8, 7, 6, 5, 4, 3, 2, 1]

if a == ascending:
    print("ascending")
elif a == descending:
    print("descending")
else:
    print("mixed")


# 리스트 뒤집기로 풀기
# a = list(map(int, input().split()))
# b = sorted(a)

# if a == b:
#     print("ascending")
# elif a == b[::-1]:
#     print("descending")
# else:
#     print("mixed")
