'''
date: 2019-07-03
'''

from collections import deque

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] #north, east, south, west

for test_case in range(1, int(input()) + 1):
    w, h = map(int, input().split())
    MAP = [list(input()) for _ in range(h)]
    Q = deque()
    visited = [[False] * w for _ in range(h)]
    dist = [[0] * w for _ in range(h)]
    sx, sy = 0, 0
    for i in range(w*h):
        x, y = i//w, i%w
        if MAP[x][y] == '*':
            Q.append((x, y, 'fire'))
            dist[x][y] = 1
        elif MAP[x][y] == '@':
            sx, sy = x, y

    def bfs():
        Q.append((sx, sy, 'dog'))
        dist[sx][sy] = 1
        while Q:
            x, y, f = Q.popleft()
            for dir in directions:
                nx, ny = x + dir[0], y + dir[1]
                if not(0 <= nx < h and 0 <= ny < w):
                    if f is 'fire':
                        continue
                    print(dist[x][y])
                    return
                if dist[nx][ny] or MAP[nx][ny] == '#':
                    continue
                dist[nx][ny] = dist[x][y] + 1
                Q.append((nx, ny, f))
        print('IMPOSSIBLE')

    bfs()