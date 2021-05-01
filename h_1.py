
def solution(n,m,dic):
    n -= len(dic)
    time = 0
    while n != 0:
        time += 1
        print(dic)
        for i in dic:
            dic[i] -= 1
            if dic[i] == 0:
                n -= 1
                if n == 0 :break
                dic[i] = i
    print(dic)
    time += max(dic.values())
    return time

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,m = map(int,input().split())

        dic = dict(map(lambda x: (int(x),int(x)),input().split()))
        print(solution(n,m,dic))