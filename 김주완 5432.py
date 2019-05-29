# sticks cut by lasers + sticks
for test_case in range(1, int(input())+1):
    pos = input()
    stack = []
    pieces, lv = 0, 0
    for i in range(len(pos)):
        if pos[i] == '(':
            lv += 1
            stack += [i]
        else:
            if i - stack.pop() == 1:
                lv -= 1
                pieces += lv
            else:
                lv -= 1
                pieces += 1
    print('#{} {}'.format(test_case, pieces))
