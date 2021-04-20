
def solution(a,b):
    return solution(b,a%b) if a%b else b 

if __name__ == '__main__':
    a,b = map(int,input().split())
    gcd = solution(a,b)
    lcm = a*b // gcd
    print(gcd)
    print(lcm)