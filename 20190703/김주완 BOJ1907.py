M = ['', '', '']
M[0], tmp = map(str, input().split('+'))
M[1], M[2] = map(str, tmp.split('='))

m = [{'C': 0, 'H': 0, 'O': 0},
     {'C': 0, 'H': 0, 'O': 0},
     {'C': 0, 'H': 0, 'O': 0}]
for i in range(3):
    for j in range(len(M[i])):
        if M[i][j] in m[0].keys():
            m[i][M[i][j]] += 1
        else:
            m[i][M[i][j-1]] += int(M[i][j]) - 1

def permutation(depth, coef):
    if depth == 3:
        if (coef[0] * m[0]['C'] + coef[1] * m[1]['C'] == coef[2] * m[2]['C']) and (coef[0] * m[0]['H'] + coef[1] * m[1]['H'] == coef[2] * m[2]['H']) and (coef[0] * m[0]['O'] + coef[1] * m[1]['O'] == coef[2] * m[2]['O']):
            return coef
        else:
            return False
    else:
        s = ''
        for i in range(1, 11):
            seq = permutation(depth+1, coef + [i])
            if seq:
                break
        return seq
ans = permutation(0, [])
print(str(ans[0]) + ' ' + str(ans[1]) + ' ' + str(ans[2]))