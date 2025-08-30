from collections import deque
import sys

sys.setrecursionlimit(100000)

n,m,v = map(int,input().split())

A = [[] for _ in range(n+1)]
visited = [False] * (n+1)


for _ in range(m):
    x,y = map(int,input().split())
    A[x].append(y)
    A[y].append(x)


def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

def BFS(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        now = queue.popleft()
        for i in A[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)