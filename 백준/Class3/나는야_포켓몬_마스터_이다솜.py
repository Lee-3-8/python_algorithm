import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n,m = map(int,input().split())
    dic = {}
    for i in range(1,n+1):
        mon = input().strip()
        dic[mon] = i
        dic[str(i)] = mon
    for i in range(m):
        qu = input().strip()
        print(dic[qu])