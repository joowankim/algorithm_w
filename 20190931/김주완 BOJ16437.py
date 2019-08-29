'''
date: 2019-08-29
'''
N = int(input())
islands = [0] * N
adj = [[] for _ in range(N)]

for i in range(1, N):
    line = input().split()
    islands[i] = int(line[1]) if line[0] == 'S' else -int(line[1])
    adj[int(line[2])-1] += [i]

def postorder(root):
    cnt = 0
    for i in adj[root]:
        cnt += postorder(i)
    return max(cnt + islands[root], 0)

print(postorder(0))

# input = __import__('sys').stdin.readline
# n = int(input())
# a = [0] * n
# a[0] = 1
# d = [0]
# p = [0]
# for i in range(n - 1):
# 	x, y, z = input().split()
# 	a[int(z) - 1] += 1
# 	d.append(int(y) if x == 'S' else -int(y))
# 	p.append(int(z) - 1)
# print('d', d)
# print('p', p)
# q = [i for i in range(n) if not a[i]]
# print('a', a)
# print('q', q)
# for i in q:
# 	d[p[i]] += max(d[i], 0)
# 	a[p[i]] -= 1
# 	if not a[p[i]]: q.append(p[i])
# print(max(d[0], 0))