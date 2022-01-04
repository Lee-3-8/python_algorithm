from collections import Counter
import sys
input = sys.stdin.readline


def solution(arr, n):
    arr.sort()
    counter = Counter(arr)
    print(round(sum(arr) / n))
    print(arr[n//2])
    most = counter.most_common(2)
    print(most[0][0] if len(most) == 1 or most[0]
          [1] > most[1][1] else most[1][0])
    print(arr[-1] - arr[0])


if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    solution(arr, n)
