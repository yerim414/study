# https://www.acmicpc.net/problem/2751
import sys
input = sys.stdin.readline

n = int(input())
A = [int(input()) for _ in range(n)]
A.sort()

sys.stdout.write("\n".join(map(str, A)))