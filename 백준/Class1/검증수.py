from functools import reduce

if __name__ == '__main__':
    inp = map(int,input().split())
    print(reduce(lambda acc,cur: acc + cur**2, inp,0)%10)
