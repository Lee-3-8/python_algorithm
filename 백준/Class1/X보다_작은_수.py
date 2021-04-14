
n,x = map(int,input().split())
arr = list(map(int,input().split()))
for i in filter(lambda k: k < x ,arr):
    print(i,end=' ')

