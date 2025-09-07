import sys
input = sys.stdin.readline

Q = int(input().strip())
for _ in range(Q):
    s = input().strip()
    count = sum(1 for i in range(len(s) - 2) if s[i:i+3] == "WOW")
    print(count)