'''
date: 2019-08-06
'''

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())
MAP = [tuple(map(int, input().split())) for _ in range(N)]

def bfs(i, j):
    global d
    Q = deque()
    Q.append((i, j))
    clean = [0] * (N*M)
    clean[i*M + j] = 1
    while Q:
        (x, y) = Q.popleft()
        all_clean = 0
        for i in range(1, 5):
            nd = (d - i) % 4
            nx, ny = x + dir[nd][0], y + dir[nd][1]
            if 0 <= nx < N and 0 <= ny < M:
                if clean[nx * M + ny] == 0 and MAP[nx][ny] == 0:
                    Q.append((nx, ny))
                    clean[nx * M + ny] = 1
                    d = nd
                    break
            all_clean += 1
        if all_clean == 4:
            nd = (d + 2) % 4
            nx, ny = x + dir[nd][0], y + dir[nd][1]
            if 0 <= nx < N and 0 <= ny < M:
                if MAP[nx][ny] == 0:
                    Q.append((nx, ny))
    return clean

print(sum(bfs(r, c)))