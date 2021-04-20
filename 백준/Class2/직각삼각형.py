
def solution(tri):
    tri.sort()
    a,b,c = tri
    return 'right' if c**2 == b**2 + a**2 else 'wrong'
    
if __name__ == '__main__':
    while True:
        tri = list(map(int,input().split()))
        if tri[0] == 0:
            break
        print(solution(tri))