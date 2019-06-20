'''
date : 2019-06-20
'''
from collections import deque

directions = [(1, 0), (0, 1), (-1, 0), (0 ,-1)]   # north, east, south, west

def bfs(i, j):
    Q = deque([(i, j)])
    global field
    field[i][j] = 0
    while Q:
        (x, y) = Q.popleft()
        for (r, c) in directions:
            nx, ny = x + r, y + c
            if 0 <= nx < N and 0 <= ny < M:
                if field[nx][ny] == 1:
                    Q.append((nx, ny))
                    field[nx][ny] = 0

for test_case in range(1, int(input()) + 1):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]

    for i in range(K):
        y, x = map(int, input().split())
        field[x][y] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)
