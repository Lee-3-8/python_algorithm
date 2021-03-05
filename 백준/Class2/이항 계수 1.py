# from math import comb

def comb(n,r,memo):
    if n == 1 or n == r or r == 0: return 1

    if r == 1: return n

    if memo[n][r] == -1:
        memo[n][r] = comb(n-1,r,memo) + comb(n-1,r-1,memo)
    return memo[n][r]


def main():
    n, r = map(int,input().split())
    memo = [[-1]*(n+1) for _ in range(n+1)]
    print( comb(n,r,memo))


if __name__=="__main__":
    main()