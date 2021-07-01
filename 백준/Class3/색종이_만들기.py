import sys
input = sys.stdin.readline

def count_num(arr,x,y):
    result = 0
    for i in range(y[0],y[1]):
        result += sum(arr[i][x[0]:x[1]])
    return result

def solution(arr,n):
    white = 0
    blue = 0
    def r_divide(x,y,n):
        nonlocal white, blue
        num = count_num(arr,x,y)
        if num == (x[1] - x[0])**2:
            blue += 1
            return
        elif num == 0:
            white += 1
            return
        elif n != 1:
            r_divide((x[0],x[0] + n//2), (y[0],y[0] + n//2), n//2)
            r_divide((x[1] - n//2,x[1]), (y[0],y[0] + n//2), n//2)
            r_divide((x[0],x[0] + n//2), (y[1] - n//2,y[1]), n//2)
            r_divide((x[1] - n//2,x[1]), (y[1] - n//2,y[1]), n//2)
    
    r_divide((0, n), (0, n),n)
    return white,blue

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    white,blue = solution(arr,n)
    print(white)
    print(blue)
