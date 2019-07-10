'''
date: 2019-07-09
'''

N = int(input())
sqrs = [pow(i, 2) for i in range(1, int(pow(N, 1/2)) + 1)]
def power_nums():
    dp = [0]*(N+1)
    for i in range(1, N+1):
        cnt = 1000001
        for n in sqrs:
            if n <= i and cnt > dp[i-n] + 1:
                cnt = dp[i-n] + 1
        dp[i] = cnt
    return dp[N]
print(power_nums())