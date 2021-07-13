
def preorder(tree,node,result): # 전위
    result[0] += node

    if tree[node]['l'] != '.':
        preorder(tree,tree[node]['l'],result)
    if tree[node]['r'] != '.':
        preorder(tree,tree[node]['r'],result)

def inorder(tree,node,result): # 중위
    
    if tree[node]['l'] != '.':
        inorder(tree,tree[node]['l'],result)

    result[1] += node

    if tree[node]['r'] != '.':
        inorder(tree,tree[node]['r'],result)

def postorder(tree,node,result): # 후위
    if tree[node]['l'] != '.':
        postorder(tree,tree[node]['l'],result)

    if tree[node]['r'] != '.':
        postorder(tree,tree[node]['r'],result)
        
    result[2] += node

if __name__ == '__main__':
    n = int(input())
    tree = {}
    for i in range(n):
        root,left,right = input().split()
        tree[root] = {
            'l':left,
            'r':right
        }
    result = ['']*3
    preorder(tree,'A',result)
    inorder(tree,'A',result)
    postorder(tree,'A',result)
    for i in result:
        print(i)
