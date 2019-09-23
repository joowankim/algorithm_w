import sys

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

R, C, T = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

def spread(map_):
    clone = [[map_[i][j] for j in range(C)] for i in range(R)]
    for i in range(R):
        for j in range(C):
            if map_[i][j] > 4:
                sp = map_[i][j] // 5
                for (dx, dy) in dirs:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < R and 0 <= ny < C:
                        if map_[nx][ny] == -1:
                            continue
                        else:
                            clone[nx][ny] += sp
                            clone[i][j] -= sp
    return clone

def air_clean_top(x):
    for i in range(x-1, 0, -1):
        A[i][0] = A[i-1][0]
    for j in range(C-1):
        A[0][j] = A[0][j+1]
    for i in range(x):
        A[i][C-1] = A[i+1][C-1]
    for j in range(C-1, 1, -1):
        A[x][j] = A[x][j-1]
    A[x][1] = 0

def air_clean_bottom(x):
    for i in range(x+1, R-1):
        A[i][0] = A[i+1][0]
    for j in range(C-1):
        A[R-1][j] = A[R-1][j+1]
    for i in range(R-1, x, -1):
        A[i][C-1] = A[i-1][C-1]
    for j in range(C-1, 1, -1):
        A[x][j] = A[x][j-1]
    A[x][1] = 0

condi = 0
for i in range(R):
    for j in range(C):
        if A[i][j] == -1:
            condi = i

for t in range(T):
    A = spread(A)
    air_clean_top(condi-1)
    air_clean_bottom(condi)
sum_ = 0
for i in range(R):
    sum_ += sum(A[i])

print(sum_+2)