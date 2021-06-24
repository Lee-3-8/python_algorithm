from collections import defaultdict,deque
import sys
sys.setrecursionlimit(15000)
input = sys.stdin.readline

def init_graph(m):
    dic = defaultdict(list)
    for i in range(m):
        start,end = map(int,input().split())
        dic[start].append(end)
        dic[end].append(start)
    return dic

def solution(n,dic):
    result = 0
    visited = set()

    def dfs(node):
        visited.add(node)
        for i in dic[node]:
            if i not in visited:
                dfs(i)

    def bfs(node):
        que = deque([node])
        while que:
            for j in dic[que.popleft()]:
                if j not in visited:
                    que.append(j)
                    visited.add(j)

    for i in range(1,n+1):
        if i not in visited:
            dfs(i)
            result += 1
    return result

if __name__ =='__main__':
    n,m = map(int, input().split())
    dic = init_graph(m)
    print(solution(n, dic))