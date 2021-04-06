# def start(dic,):


def solution(arr,m):
    mon_arr = [10001 for i in range(m+1)]
    mon_arr[0] = 0
    for i in arr:
        for j in range(i,m+1):
            if mon_arr[j-i] != 10001:
                mon_arr[j] = min(mon_arr[j],mon_arr[j-i]+1)
    return -1 if mon_arr[m] == 10001 else mon_arr[m] 

if __name__ == '__main__':
    n, m = map(int,input().split())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    print(solution(arr,m))