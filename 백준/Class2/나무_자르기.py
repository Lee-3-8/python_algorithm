import sys

input = sys.stdin.readline

def solution(arr,m):
    start = 0
    end = max(arr)
    result = 0
    while start <= end:
        total = 0
        mid = (start+end) // 2
        for i in arr:
            if i > mid:
                total += i-mid
        if total < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result

if __name__ =='__main__':
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    print(solution(arr,m))