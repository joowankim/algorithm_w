'''
date: 2019-06-20
'''

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] #north, east, south, west
from collections import deque
def bfs(i, j, visit):
    global MAP
    Q = deque([(i, j)])
    visit[i][j] = True
    while Q:
        (x, y) = Q.popleft()
        for (r, c) in directions:
            nx, ny = x + r, y + c
            if 0 <= nx < N and 0 <= ny < M:
                if not visit[nx][ny] and MAP[nx][ny] == 0:
                    Q.append((nx, ny))
                    visit[nx][ny] = True

def dfs(h, pre):
    global counts
    if h == 3:
        visit = [[False] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if MAP[i][j] == 2:
                    bfs(i, j, visit)
                elif MAP[i][j] == 1:
                    visit[i][j] = True
        cnt = 0
        for i in range(N):
            for j in range(M):
                if not visit[i][j]:
                    cnt += 1
        counts += [cnt]

    else:
        for i in range(pre, N*M):
            x = int(i/M)
            y = int(i%M)
            if MAP[x][y] == 0:
                MAP[x][y] = 1
                dfs(h+1, i)
                MAP[x][y] = 0

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
counts = []
dfs(0, 0)
print(max(counts))