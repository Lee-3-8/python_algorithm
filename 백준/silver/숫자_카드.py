import sys
input = sys.stdin.readline

def solution(have,find):
    return list(map(lambda x: int(x in have),find))

if __name__ == '__main__':
    n = int(input())
    have = set(map(int,input().split()))
    m = int(input())
    find = list(map(int,input().split()))
    print(*solution(have,find))