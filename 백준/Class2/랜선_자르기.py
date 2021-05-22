import sys

input = sys.stdin.readline

def solution(arr,m):
    result = 0
    start = 1
    end = max(arr)
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in arr:
            total += (i // mid)
        if total < m: # 자르는 기준이 너무크다
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result

if __name__ =='__main__':
    n,m = map(int,input().split())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    print(solution(arr,m))