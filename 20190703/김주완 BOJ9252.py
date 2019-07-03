'''
date : 2019-06-28
'''
seq1 = input()
seq2 = input()

n, m = len(seq1), len(seq2)
dp = [[[0, ''] for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if seq1[i-1] == seq2[j-1]:
            dp[i][j][0] = dp[i-1][j-1][0] + 1
            dp[i][j][1] = dp[i-1][j-1][1] + seq1[i-1]
        else:
            if dp[i-1][j][0] > dp[i][j-1][0]:
                dp[i][j][0] = dp[i-1][j][0]
                dp[i][j][1] = dp[i-1][j][1]
            else:
                dp[i][j][0] = dp[i][j-1][0]
                dp[i][j][1] = dp[i][j-1][1]
print(dp[n][m][0])
print(dp[n][m][1])
