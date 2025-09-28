# https://www.acmicpc.net/problem/2606
# DFS

import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

N = int(input())
M = int(input())

computer = [[] for _ in range(N+1)]
visited = [False] * (N+1)

def DFS(v):
    visited[v] = True
    for i in computer[v]:
        if not visited[i]:
            DFS(i)

for _ in range(M):
    s, e = map(int, input().split())
    computer[s].append(e)
    computer[e].append(s)
   
DFS(1)
print(visited.count(True) - 1)