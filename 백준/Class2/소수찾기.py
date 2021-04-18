from functools import reduce

def solution(arr):
    max_num = max(arr)
    # int(max(arr) ** 0.5) + 1
    che = set([i for i in range(2,max_num + 1)])
    del_che = [2,3,5,7,11,13,17,19,23,29,31]
    for i in del_che:
        r_max = int(max(arr) ** 0.5) + 1
        print(r_max)
        if i > r_max:
            break
        for j in range(2*i, max_num + 1,i):
            che.discard(j)
    print(che)
    return reduce(lambda acc,cur : acc + (1 if cur in che else 0),arr,0)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    print(solution(arr))