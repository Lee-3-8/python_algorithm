import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n,m = map(int,input().split())
    set_a = set()
    set_b = set()
    for i in range(1,n+1):
        p = input().strip()
        set_a.add(p)
    for i in range(m):
        p = input().strip()
        set_b.add(p)
    set_c = set_a & set_b
    print(len(set_c))
    for i in sorted(list(set_c)):
        print(i)