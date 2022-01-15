
def solution(n, m):

    def dfs(cur):
        if len(cur) == m:
            print(*cur)
        else:
            for i in range(1, n+1):
                if i not in cur:
                    dfs(cur + [i])

    for i in range(1, n+1):
        dfs([i])


if __name__ == "__main__":
    n, m = map(int, input().split())
    solution(n, m)
