
def get_sum(r,c,flag):
    result = 0
    dic = {
        1:"WBWBWBWB",
        -1:"BWBWBWBW"
    }
    for i in range(r,8+r):
        ans = dic[flag]
        flag *= -1
        for j in range(8):
            if arr[i][j+c] != ans[j]:
                result += 1
    return result

def solution(n,m,arr):
    result = get_sum(0,0,1)
    print(result)
    for i in range(n-7): #2
        for j in range(m-7): #6
            result = min(result,get_sum(i,j,1))
            result = min(result,get_sum(i,j,-1))
            print(i,j,result)

    return result

if __name__ == '__main__':
    n,m = map(int,input().split())
    arr = []
    for i in range(n):
        raw = input()
        arr.append(raw)
    print(solution(n,m,arr))