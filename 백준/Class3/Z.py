import sys
input = sys.stdin.readline

def solution(n,r,c):
    if r == 0 and c == 0: return 0
    visited = {}
    cnt = 0

    def dfs(m,x1,x2,y1,y2):
        if (r,c) in visited: return
        nonlocal cnt
        if not (y1 <= r <= y2 and x1 <= c <= x2):
            cnt += 2**(2*m)
            return
        if m == 1:
            visited[(y1,x1)] = cnt
            visited[(y1,x2)] = cnt+1
            visited[(y2,x1)] = cnt+2
            visited[(y2,x2)] = cnt+3
            cnt += 4
            return

        dfs(m-1,x1, x2 - 2**(m-1), y1, y2 - 2**(m-1))
        dfs(m-1,x1 + 2**(m-1), x2, y1, y2 - 2**(m-1))
        dfs(m-1,x1, x2 - 2**(m-1), y1 + 2**(m-1), y2)
        dfs(m-1,x1 + 2**(m-1), x2, y1 + 2**(m-1), y2)

    dfs(n, 0, 2**n - 1, 0, 2**n - 1)
    return visited[(r,c)]

if __name__ == '__main__':
    n,r,c = map(int,input().split())
    print(solution(n,r,c))