from collections import defaultdict

def solution(dic):
    result = set()
    
    def dfs(start):
            for i in dic[start]:
                if i not in result:
                    result.add(i)
                    dfs(i)

    dfs(1)
    return len(result) -1 

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    dic = defaultdict(list)
    for i in range(m):
        s,e = map(int,input().split())
        dic[s].append(e)
        dic[e].append(s)
    print(solution(dic))