from collections import deque

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
pos = []
for i in range(N):
    for j in range(N):
        if MAP[i][j] == 2:
            pos += [(i, j)]
            MAP[i][j] = -1

def combi(depth, virus, last):
    if depth == M:
        clone = [[MAP[i][j] for j in range(N)] for i in range(N)]
        t = spread(virus, clone)
        return t
    else:
        min_ = N*N + 1
        for i in range(last+1, len(pos)):
            t = combi(depth+1, virus + [pos[i]], i)
            if min_ > t:
                min_ = t
        return min_

def spread(virus, clone):
    Q = deque()
    for (i, j) in virus:
        Q.append((i, j, 0))
        clone[i][j] = 2
    t = 0
    while Q:
        (x, y, ti) = Q.popleft()
        for (dx, dy) in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if clone[nx][ny] == 0:
                    clone[nx][ny] = ti + 1
                    Q.append((nx, ny, clone[nx][ny]))
                    t = clone[nx][ny]
                elif clone[nx][ny] == -1:
                    clone[nx][ny] = ti + 1
                    Q.append((nx, ny, clone[nx][ny]))
    success = True
    for i in range(N*N):
        x, y = i//N, i%N
        if clone[x][y] == 0:
            success = False
            break
    if success:
        return t
    else:
        return N*N

ans = combi(0, [], -1)
if ans == N*N:
    print(-1)
else:
    print(ans)
