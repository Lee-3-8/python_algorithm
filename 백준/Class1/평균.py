
def solution(n,arr):
    m = max(arr)
    return sum(map(lambda x: x/m*100,arr)) /len(arr)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    print(solution(n,arr))