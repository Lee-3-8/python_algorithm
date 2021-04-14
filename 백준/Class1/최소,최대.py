
N = int(input())
for i in range(N):
    arr = input()
    cnt = 0
    result = 0
    for j in arr:
        if j == 'O':
            cnt+=1
            result += cnt
        else:
            cnt = 0
    print(result)