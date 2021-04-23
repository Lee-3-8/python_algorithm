import sys

input = sys.stdin.readline

def fibonacci(n):
    if dp[n] == -1:
        n_1 = dp[n-1] if dp[n-1] != -1 else fibonacci(n-1)
        n_2 = dp[n-2] if dp[n-2] != -1 else fibonacci(n-2)
        dp[n] = n_1 + n_2
    return dp[n]

if __name__ == '__main__':
    t = int(input())
    dp = [-1]*41
    dp[0],dp[1] = 0,1
    for i in range(t):
        n = int(input())
        if n == 0: print(1,0)
        else:
            fibonacci(n)
            print(dp[n-1],dp[n])