
def solution(n):
    result = {}
    for num in range(1, n + 1):
        calced = num + sum(map(int, str(num)))
        if calced not in result:
            result[calced] = num
    return result.get(n, 0)


if __name__ == "__main__":
    n = int(input())
    print(solution(n))
