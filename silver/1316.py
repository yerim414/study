# https://www.acmicpc.net/problem/1316
import sys
input = sys.stdin.readline

n = int(input())
count = 0  # 그룹 단어 개수 세기

for _ in range(n):
    word = input().strip()
    seen = set()   # 이미 등장한 문자들
    prev = ''      # 이전 글자
    is_group = True

    for ch in word:
        if ch != prev:
            if ch in seen:
                is_group = False
                break
            seen.add(ch)
        prev = ch

    if is_group:
        count += 1

print(count)
