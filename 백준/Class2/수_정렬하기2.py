import sys

input = sys.stdin.readline
if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    for i in sorted(arr):
        print(i)