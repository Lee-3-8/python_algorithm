from bisect import bisect_left,bisect_right

def solution(arr,x):
    bl = bisect_left(arr,x)
    br = bisect_right(arr,x)
    return -1 if br-bl == 0 else br - bl

if __name__ =='__main__':
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    print(solution(arr,m))