'''
date : 2019-06-30
'''

N = int(input())
K = int(input())
apples = [tuple(map(int, input().split())) for _ in range(K)]
L = int(input())
turns = [list(input().split()) for _ in range(L)]
for i in range(L):
    turns[i][0] = int(turns[i][0])

board = [[0] * N for _ in range(N)]
for (x, y) in apples:
    board[x-1][y-1] = 2

end = False
secs = 0
turn = 0
dir = [0, 1]
snake = [(0, 0)]
while not end:
    if turns[turn][0] == secs:
        if dir[0] == 0:
            if turns[turn][1] == 'L':
                tmp = dir[0]
                dir[0] = -dir[1]
                dir[1] = -tmp
            else:
                tmp = dir[0]
                dir[0] = dir[1]
                dir[1] = tmp
        elif dir[1] == 0:
            if turns[turn][1] == 'D':
                tmp = dir[0]
                dir[0] = -dir[1]
                dir[1] = -tmp
            else:
                tmp = dir[0]
                dir[0] = dir[1]
                dir[1] = tmp
        if turns[turn][0] < turns[-1][0]:
            turn += 1
    (x, y) = snake[-1]
    nx, ny = x + dir[0], y + dir[1]
    if 0 <= nx < N and 0 <= ny < N:
        if board[nx][ny] == 2:
            board[nx][ny] = 1
            snake += [(nx, ny)]
        elif board[nx][ny] == 1:
            end = True
        elif board[nx][ny] == 0:
            board[nx][ny] = 1
            snake += [(nx, ny)]
            (tx, ty) = snake[0]
            board[tx][ty] = 0
            del snake[0]
    else:
        end = True
    secs += 1
print(secs)