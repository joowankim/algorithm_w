'''
date: 2019-09-10
'''

N = int(input())
root = -1
node = [[] for _ in range(N)]
parents = list(map(int, input().split()))
for (i, parent) in enumerate(parents):
    if parent == -1:
        root = i
    else:
        node[parent] += [i]

def dfs(r):
    if node[r] == []:
        return 1
    else:
        cnt = 0
        for i in node[r]:
            cnt += dfs(i)
        return cnt

del_node = int(input())
if del_node == root:
    print(0)
else:
    node[parents[del_node]].remove(del_node)
    print(dfs(root))



