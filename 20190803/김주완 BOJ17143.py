'''
date: 2019-08-01
'''

import sys

dir = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]

R, C, M = map(int, sys.stdin.readline().split())

sharks = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

dead = [False] * M
pool = [[-1] * C for _ in range(R)]

idx = 0
for [r, c, s, d, z] in sharks:
    pool[r-1][c-1] = idx
    idx += 1

weight = 0
for j in range(C):
    for i in range(R):
        if pool[i][j] != -1:
            weight += sharks[pool[i][j]][4]
            dead[pool[i][j]] = True
            pool[i][j] = -1
            break
    move = [False] * M
    for shark_idx in range(M):
        if not dead[shark_idx]:
            [r, c, s, d, z] = sharks[shark_idx]
            nx, ny = r-1 + dir[d][0]*s, c-1 + dir[d][1]*s
            while True:
                if nx < 0:
                    d = 2
                    nx = -nx
                elif nx > (R-1):
                    d = 1
                    nx = (R-1) - (nx - (R-1))
                if ny < 0:
                    d = 3
                    ny = -ny
                elif ny > (C-1):
                    d = 4
                    ny = (C-1) - (ny - (C-1))
                if 0 <= nx < R and 0 <= ny < C:
                    break
            if pool[r-1][c-1] == shark_idx:
                pool[r-1][c-1] = -1

            move[shark_idx] = True
            sharks[shark_idx][0], sharks[shark_idx][1], sharks[shark_idx][3] = nx+1, ny+1, d
            if pool[nx][ny] != -1:
                if not move[pool[nx][ny]]:
                    pool[nx][ny] = shark_idx
                else:
                    if sharks[pool[nx][ny]][4] < z:
                        dead[pool[nx][ny]] = True
                        pool[nx][ny] = shark_idx
                    elif sharks[pool[nx][ny]][4] > z:
                        dead[shark_idx] = True
            else:
                pool[nx][ny] = shark_idx

print(weight)