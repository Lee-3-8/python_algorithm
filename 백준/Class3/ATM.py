import sys
input = sys.stdin.readline

def solution(arr):
    arr.sort()
    result = map(lambda x: arr[x]*(len(arr) - x),range(len(arr)))
    return sum(result)

if __name__ == '__main__':
    n = map(int,input().split())
    arr = list(map(int,input().split()))
    print(solution(arr))