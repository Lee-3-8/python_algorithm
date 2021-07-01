
def solution(n):
    dp = {}
    def dfs(n):
        if n in dp:
            return dp[n]
        if n == 0 or n == 1:
            return 1
        if n > 1:
            dp[n] = dfs(n-2) + dfs(n-1)
            return dp[n]
    
    return dfs(n) % 10007

if __name__ == '__main__':
    n = int(input())
    print(solution(n))