'''
date: 2019-07-09
'''

for test_case in range(int(input())):
    n = int(input())
    st = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0] * n for _ in range(2)]
    dp[0][0] = st[0][0]
    dp[1][0] = st[1][0]
    dp[0][1] = dp[1][0] + st[0][1]
    dp[1][1] = dp[0][0] + st[1][1]

    for i in range(2, n):
        dp[0][i] = st[0][i] + max(dp[1][i-1], max(dp[0][i-2], dp[1][i-2]))
        dp[1][i] = st[1][i] + max(dp[0][i-1], max(dp[0][i-2], dp[1][i-2]))

    print(max(dp[0][n-1], dp[1][n-1], dp[0][n-2], dp[1][n-2]))


