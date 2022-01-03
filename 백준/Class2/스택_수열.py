import sys
input = sys.stdin.readline


def solution(n, arr):
    stack = [1]
    cnt = 1
    result = ["+"]
    for num in arr:
        while (not stack or stack[-1] < num):
            cnt += 1
            stack.append(cnt)
            result.append("+")
        if stack[-1] == num:
            stack.pop()
            result.append("-")
        else:
            print("NO")
            return
    for i in result:
        print(i)


if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    solution(n, arr)
