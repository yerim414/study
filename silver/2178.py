# https://www.acmicpc.net/problem/2178?utm_source=chatgpt.com
# BFS

from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 체크 (미로 안에 있는지)
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
                
            # 아직 방문하지 않은 길(1)일 때
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1 # 거리 누적
                queue.append((nx, ny))

    return maze[N-1][M-1]

print(BFS(0, 0))