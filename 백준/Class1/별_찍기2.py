
def solution(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if n-i < j:
                print('*',end='')
            else:
                print(' ',end='')
        print()

if __name__ == '__main__':
    n = int(input())
    solution(n)