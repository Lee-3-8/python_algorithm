
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        h,w,n = map(int,input().split())
        chng, ho = n%h, n//h + 1
        if chng == 0:
            chng = h
            ho = n//h
        # (n//h) +1 ->호수  n%h -> 층
        print(f'{chng*100+ho}')