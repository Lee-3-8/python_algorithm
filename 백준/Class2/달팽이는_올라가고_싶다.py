import math


def solution(a, b, v):
    x = 0
    return math.ceil((v - a) / (a-b)) + 1


if __name__ == "__main__":
    a, b, v = map(int, input().split())
    print(solution(a, b, v))
