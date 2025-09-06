import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())

# 1 BASE
A = [[] for _ in range(n + 1)]
visited = [False] * (n+1)

for _ in range(m):
    u,v = map(int, input().split())
    A[u].append(v)
    A[v].append(u)


def DFS(n):
    visited[n] = True
    for i in A[n]:
        if not visited[i]:
            DFS(i)

count = 0
for i in range(1, n + 1):
    if not visited[i]:
        count += 1
        DFS(i)

print(count)