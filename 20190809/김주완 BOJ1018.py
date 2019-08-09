'''
date: 2019-08-07
'''

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
MAP = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        MAP[i][j] = 1 if board[i][j] == 'B' else 0

def filter1(x, y):
    filter = [[1, 0, 1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1, 0, 1]]
    cnt = 0
    for i in range(8):
        for j in range(8):
            cnt += filter[i][j] ^ MAP[x+i][y+j]
    return cnt

def filter2(x, y):
    filter = [[0, 1, 0, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 0, 1, 0]]
    cnt = 0
    for i in range(8):
        for j in range(8):
            cnt += filter[i][j] ^ MAP[x+i][y+j]
    return cnt

ans = M*N
for i in range(N-7):
    for j in range(M-7):
        tmp = min(filter1(i, j), filter2(i, j))
        if ans > tmp:
            ans = tmp
print(ans)