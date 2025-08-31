# https://www.acmicpc.net/problem/11403
import sys
sys.setrecursionlimit(10000)

G = int(input())
adj = [list(map(int, input().split())) for _ in range(G)]
result = [[0] * G for _ in range(G)]

def DFS(start, v, visited):
    # print("DFS 탐색중 ", result, "start - ", start, "v - ", v)
    for i in range(G):
        if adj[v][i] == 1 and not visited[i]:
            visited[i] = True
            result[start][i] = 1
            DFS(start, i, visited)


for i in range(G):
    visited = [False] * G
    DFS(i, i, visited)

for row in result:
    print(*row)