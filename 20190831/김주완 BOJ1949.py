'''
date: 2019-08-30
'''

N = int(input())
nums = list(map(int, input().split()))
tmp = [tuple(map(int, input().split())) for _ in range(N-1)]
adj = [[] for _ in range(N)]

for (i, j) in tmp:
    adj[i-1] += [j-1]
    adj[j-1] += [i-1]

visited = [False] * N

def dfs(vill, flag):
    cnt = 0
    visited[vill] = True

    for i in range(len(adj[vill])):
        next = adj[vill][i]
        if visited[next]:
            continue
        if flag:
            cnt += dfs(next, 0)
        else:
            cnt += max(dfs(next, 0), dfs(next, 1) + nums[next])
    visited[vill] = False
    return cnt

print(max(dfs(0, 0), dfs(0, 1) + nums[0]))
