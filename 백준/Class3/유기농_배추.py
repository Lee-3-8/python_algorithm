import sys;
sys.setrecursionlimit(10000)

def dfs(bechu,y,x,i,j):
    if j < 0 or i < 0 or j >= x or i >= y:
        return 0
    if bechu[i][j] == 1:
        bechu[i][j] = 0
        dfs(bechu,y,x,i-1,j)
        dfs(bechu,y,x,i+1,j)
        dfs(bechu,y,x,i,j-1)
        dfs(bechu,y,x,i,j+1)
        return 1
    return 0

def solution(bechu,x,y):
    cnt = 0
    for i in range(y):
        for j in range(x):
            cnt += dfs(bechu,y,x,i,j)
    return cnt

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        x,y,k = map(int,input().split())
        bechu = [[0]*(x) for _ in range(y)]
        for _ in range(k):
            j,i = map(int,input().split())
            bechu[i][j] = 1
        print(solution(bechu,x,y))
