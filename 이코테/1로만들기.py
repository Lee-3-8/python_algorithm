
def solution(x):
    arr = [0]*(x+1)
    cmd_5 = lambda x:arr[x // 5] if x%5 == 0 else float('inf')
    cmd_3 = lambda x:arr[x // 3] if x%3 == 0 else float('inf')
    cmd_2 = lambda x:arr[x // 2] if x%2 == 0 else float('inf')

    for i in range(2,x+1):
        arr[i] = min(cmd_2(i),cmd_3(i),cmd_5(i),arr[i-1]) + 1
    
    return arr[x]

if __name__ == '__main__':
    x = int(input())
    print(solution(x)) 