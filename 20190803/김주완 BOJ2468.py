'''
date: 2019-08-01
'''

from queue import Queue

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

def bfs(i, j, height, visited):
    Q = Queue()
    Q.put((i, j))
    visited[i][j] = True
    while not Q.empty():
        (x, y) = Q.get()
        for dir in directions:
            nx, ny = x + dir[0], y + dir[1]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and MAP[nx][ny] > height:
                    Q.put((nx, ny))
                    visited[nx][ny] = True

cnt = [0] * 100
for h in range(100):
    v = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not v[i][j] and MAP[i][j] > h:
                bfs(i, j, h, v)
                cnt[h] += 1
    if cnt[h] == 0:
        break
print(max(cnt))