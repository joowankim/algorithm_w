'''
date: 2019-08-01
'''

N = int(input())

def dfs(depth, seq, last):
    if depth == N:
        for i in range(1, int(depth/2)+1):
            if seq[depth-i:] == seq[depth-2*i:depth-i]:
                return -1
        return int(seq)
    else:
        for i in range(1, int(depth/2)+1):
            if seq[depth-i:] == seq[depth-2*i:depth-i]:
                return -1
        for i in range(1, 4):
            if last != i:
                r = dfs(depth+1, seq + str(i), i)
                if r != -1:
                    return r
        return -1

print(dfs(0, "", 0))