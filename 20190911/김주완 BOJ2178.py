'''
date: 2019-09-06
'''
from collections import deque

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N, M = map(int, input().split())
MAP = [list(map(int, list(input()))) for _ in range(N)]

def bfs():
    Q = deque([(0, 0)])
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1

    while Q:
        (x, y) = Q.popleft()
        for (dx, dy) in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and MAP[nx][ny] == 1:
                    Q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    return visited[N-1][M-1]

print(bfs())
