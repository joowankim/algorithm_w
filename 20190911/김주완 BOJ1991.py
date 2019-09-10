'''
date: 2019-09-10
'''

N = int(input())
node = dict()
for _ in range(N):
    line = input().split()
    node[line[0]] = [line[1], line[2]]

def preorder(root):
    print(root, end='')
    if node[root][0] != '.':
        preorder(node[root][0])
    if node[root][1] != '.':
        preorder(node[root][1])

def inorder(root):
    if node[root][0] != '.':
        inorder(node[root][0])
    print(root, end='')
    if node[root][1] != '.':
        inorder(node[root][1])

def postorder(root):
    if node[root][0] != '.':
        postorder(node[root][0])
    if node[root][1] != '.':
        postorder(node[root][1])
    print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')