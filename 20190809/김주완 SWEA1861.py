'''
date: 2019-08-09
'''

for test_case in range(1, int(input())+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    rooms = [(-1, -1)] * (N*N+1)

    for i in range(N):
        for j in range(N):
            rooms[MAP[i][j]] = (i, j)

    m_idx = 0
    idx = 1
    cnt = 0
    max_ = 0
    for i in range(1, N*N):
        if (rooms[i][0] - rooms[i+1][0]) + (rooms[i][1] - rooms[i+1][1]) == -1:
            if cnt == 0:
                idx = i
            cnt += 1
        else:
            if max_ < cnt:
                max_ = cnt
                m_idx = idx
            cnt = 0
    if max_ < cnt:
        max_ = cnt
        m_idx = idx

    print("#{} {} {}".format(test_case, m_idx, max_))
