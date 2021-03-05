from itertools import combinations
def main():
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    sum_arr = []
    for i in list(combinations(arr,3)):
        temp = sum(i)
        if temp <= m:
            sum_arr.append(temp)
    print( max(sum_arr) )
    return

if __name__=="__main__":
    main()