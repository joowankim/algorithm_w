'''
date: 2019-08-01
'''

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

from collections import deque

N, M = map(int, input().split())
MAP = [list(input()) for _ in range(N)]

walls = []
for i in range(N):
    for j in range(M):
        if MAP[i][j] == '1':
            walls += [(i, j)]

visited = [[[0, 0] for _ in range(M)] for _ in range(N)]

def bfs(i, j):
    Q = deque()
    Q.append((i, j, 0))
    visited[i][j][0] = 1
    while Q:
        (x, y, crash) = Q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][crash]
        for dir in directions:
            nx, ny = x + dir[0], y + dir[1]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny][crash]:
                    if MAP[nx][ny] == '0':
                        visited[nx][ny][crash] = visited[x][y][crash] + 1
                        Q.append((nx, ny, crash))
                    if MAP[nx][ny] == '1' and crash == 0:
                        visited[nx][ny][1] = visited[x][y][crash] + 1
                        Q.append((nx, ny, 1))
    return -1

print(bfs(0, 0))