'''
date: 2019-07-09
'''

import sys

N, K = map(int, sys.stdin.readline().split())
pack = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

def knap():
    dp = [[0] * (K+1) for _ in range(N+1)]

    for i in range(N+1):
        for j in range(K+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif pack[i-1][0] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-pack[i-1][0]] + pack[i-1][1])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[N][K]
print(knap())