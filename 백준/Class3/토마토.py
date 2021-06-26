from collections import deque
import sys
input = sys.stdin.readline

def solution(m,n,arr):
    result = -1
    adjacent = [(0,1),(0,-1),(1,0),(-1,0)]
    visited = set()
    que = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                que.append((i,j))

    while que:
        que.append(False)
        result += 1
        while que[0]:
            i,j = que.popleft()
            arr[i][j] = 1
            for x,y in adjacent:
                if (0<= x+i < n) and (0 <= y+j < m):
                    if arr[x+i][y+j] == -1:
                        continue
                    elif arr[x+i][y+j] == 0:
                        if (x+i,y+j) not in visited:
                            que.append((x+i,y+j))
                            visited.add((x+i,y+j))
        que.popleft()

    for i in arr:
        for j in i:
            if j == 0:
                return -1
    return result

if __name__ == '__main__':
    m,n = map(int,input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int,input().split())))
    print(solution(m,n,arr))