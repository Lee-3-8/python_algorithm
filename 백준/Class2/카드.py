from collections import deque

def solution(n):
    arr = deque([ i for i in range(1 ,n + 1)])
    while len(arr) != 1:
        arr.popleft()
        arr.append(arr.popleft())
    return arr[0]


if __name__ == '__main__':
    n = int(input())
    print(solution(n))