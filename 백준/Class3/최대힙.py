import sys
import heapq
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        k = int(input())
        if k == 0:
            if len(arr) == 0:
                print(0)
            else:
                print(-1 * heapq.heappop(arr))
        else:
            heapq.heappush(arr, -1 * k)
