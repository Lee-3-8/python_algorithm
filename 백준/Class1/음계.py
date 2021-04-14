up = [i for i in range(1,8+1)]
down = [i for i in range(8,1-1,-1)]

arr = list(map(int,input().split()))
if up == arr:
    print('ascending')
elif down == arr:
    print('descending')
else:
    print('mixed')
