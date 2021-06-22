
def solution(arr):
    result = []
    dp = {}
    
    def dfs(n):
        if n == 0:
            return 1
        if n in dp:
            return dp[n]
        cnt = 0
        for i in [1,2,3]:
            if n >= i:
                cnt += dfs(n - i)
        dp[n] = cnt
        return dp[n]

    dfs(max(arr))
    for i in arr:
        print(dp[i])

if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        k = int(input())
        arr.append(k)
    solution(arr)