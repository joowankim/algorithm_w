'''
date: 2019-08-06
'''

dir = [(0, 1), (0, -1), (-1, 0), (1, 0)]

N, M, x, y, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
cmds = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]   # 1, 2, 3, 4, 5, 6

for cmd in cmds:
    nx, ny = x + dir[cmd-1][0], y + dir[cmd-1][1]
    if 0 <= nx < N and 0 <= ny < M:
        if cmd == 1:
            dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
        elif cmd == 2:
            dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
        elif cmd == 3:
            dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
        elif cmd == 4:
            dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

        if MAP[nx][ny] == 0:
            MAP[nx][ny] = dice[5]
        else:
            dice[5] = MAP[nx][ny]
            MAP[nx][ny] = 0
        x, y = nx, ny

        print(dice[0])
