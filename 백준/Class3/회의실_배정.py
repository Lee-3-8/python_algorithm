
import sys
input = sys.stdin.readline

def solution(arr):
    check = 0
    last = -1
    for end, start in arr:
        if start >= last:
            check += 1
            last = end
    return check
if __name__ == '__main__':
    arr = []
    n = int(input())
    for i in range(n):
        start, end = map(int,input().split())
        arr.append((end,start))
    print(solution(sorted(arr)))
