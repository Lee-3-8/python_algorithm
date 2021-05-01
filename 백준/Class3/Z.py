
def r_z(arr,start,end):
    if arr[][]
    if end - start == 1:
        arr[start][start] = arr[start-1][end] + 1
        arr[start+1][start] = arr[end][start] + 1
        arr[start][end] = arr[start+1][start] + 1
        arr[end][end] = arr[start][end] + 1
    else:
        r_z(arr,start,end//2)
        r_z(arr,end//2 + 1,end)

def solution(N,r,c):
    arr = [[0]*N for _ in range(N)]
    r_z(arr,0,2**N-1)
    return 23

if __name__ == '__main__':
    N,r,c = map(int,input().split())
    print(solution(N,r,c))