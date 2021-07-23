import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def soultion(dic,n):
    # 각 점에서 모든 점까지의 깊이 합이 최소인 점을 찾자
    result = []

    def bfs(start):
        que = deque([start])
        dist = {start:0}
        while que:
            prev = que.popleft()
            for node in dic[prev]:
                if node not in dist:
                    dist[node] = dist[prev] + 1
                    que.append(node)
        return sum([i for i in dist.values()])

    for i in range(1,n+1):
        result.append(bfs(i))
    
    return result.index(min(result)) + 1

if __name__ == '__main__':
    n,m = map(int,input().split())
    dic = defaultdict(list)
    for i in range(m):
        a,b = map(int,input().split())
        dic[a].append(b)
        dic[b].append(a)
    print(soultion(dic,n))

