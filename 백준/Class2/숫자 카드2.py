import sys
from collections import Counter

def solution(n, m, n_arr, m_arr):
    dic = Counter(n_arr)
    return list(map(lambda x: dic.get(x,0), m_arr))

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    n_arr = list(map(int,sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    m_arr = list(map(int,sys.stdin.readline().split()))
    result = solution(n, m, n_arr, m_arr)
    for i in result:
        print(i,end=' ')
