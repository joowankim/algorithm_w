from collections import deque

def bfs(adj, n):
    Q = deque([(0, 0)])
    visited = [-1] * n
    visited[0] = 0
    while Q:
        (node, depth) = Q.popleft()
        for i in adj[node]:
            if visited[i] == -1:
                Q.append((i, depth+1))
                visited[i] = depth+1
    
    return visited.count(max(visited))

def solution(n, edge):
    adj = [[] for _ in range(n)]
    for [i, j] in edge:
        adj[i-1] += [j-1]
        adj[j-1] += [i-1]
    answer = bfs(adj, n)
    return answer
