
def solution(n):
    dp = [0, 5001, 5001, 1, 5001, 1] + [5001]*(n-5)

    for i in range(6, n+1):
        if dp[i-5] == 5001 and dp[i-3] == 5001:
            continue
        else:
            dp[i] = min(dp[i-5], dp[i-3]) + 1
    return -1 if dp[n] == 5001 else dp[n]


if __name__ == "__main__":
    n = int(input())
    print(solution(n))
