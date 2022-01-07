
def solution(n):
    dp = [(0, 1)]
    for i in range(1, n):
        dp.append((dp[i-1][1], sum(dp[i-1])))
    return dp[n-1]


if __name__ == "__main__":
    result = solution(int(input()))
    print(f"{result[0]} {result[1]}")
