from collections import defaultdict,deque

def solution(dic, n, v):

    def dfs(v,n,visited):
        visited[v] = v
        for i in sorted(dic[v]):
            if i not in visited:
                dfs(i,n,visited)
        return visited.keys()

    def bfs():
        que = deque([v])
        visited = dict({v:v})
        while que:
            for i in sorted(dic[que.popleft()]):
                if i not in visited:
                    que.append(i)
                    visited[i] = i
        return visited.keys()

    print(*dfs(v,n,{}))
    print(*bfs())

if __name__ == '__main__':
    n,m,v = map(int,input().split())
    dic = defaultdict(list)
    for i in range(m):
        a,b = map(int,input().split())
        dic[a].append(b)
        dic[b].append(a)
    solution(dic, n, v)