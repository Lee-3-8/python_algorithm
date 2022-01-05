
def solution(n, arr):
    dp = [0]*n
    for i in range(n):
        if i == 0:
            dp[0] = arr[0]
        elif i == 1:
            dp[1] = arr[0] + arr[1]
        elif i == 2:
            dp[2] = max(arr[0]+arr[2], arr[1]+arr[2])
        else:
            dp[i] = max(dp[i - 3] + arr[i - 1], dp[i - 2]) + arr[i]
    return dp[n-1]


if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    print(solution(n, arr))
