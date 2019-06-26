N = int(input())    # 2<=N<=50
pred = [list(map(int, input().split())) for _ in range(N)]

def dfs(depth, order):
    if depth == 9:
        score = 0
        cur = 0
        for i in range(N):
            state = [0, 0, 0]
            out = 0
            while True:
                if out == 3:
                    break
                if pred[i][order[cur]] == 0:
                    out += 1
                    cur = (cur+1)%9
                elif pred[i][order[cur]] == 1:
                    state += [1]
                    cur = (cur+1)%9
                elif pred[i][order[cur]] == 2:
                    state += [1, 0]
                    cur = (cur+1)%9
                elif pred[i][order[cur]] == 3:
                    state += [1, 0, 0]
                    cur = (cur+1)%9
                elif pred[i][order[cur]] == 4:
                    state += [1, 0, 0, 0]
                    cur = (cur+1)%9
            score += sum(state[:-3])
        return score
    elif depth == 3:
        return dfs(depth+1, order+[0])
    else:
        max_score = 0
        for i in range(1, 9):
            if i in order:
                continue
            cur = dfs(depth+1, order+[i])
            if max_score < cur:
                max_score = cur
        return max_score

print(dfs(0, []))
