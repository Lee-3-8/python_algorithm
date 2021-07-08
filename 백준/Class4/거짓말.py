
from collections import defaultdict, deque

def solution(n, parties, known, person):
    result = 0
    def bfs(start):
        que = deque([start])
        visited = set()
        while que:
            if que[0] in known: return True
            for i in list(person[que.popleft()]):
                if i not in visited:
                    que.append(i)
                    visited.add(i)
        return False

    for i in range(1,n+1):
        if bfs(i):
            known.add(i)

    for party in parties:
        if not (party & known):
            result += 1

    return result

if __name__ == '__main__':
    n,m = map(int,input().split())
    person = defaultdict(set)
    parties = []
    cnt = 0
    known = set(list(map(int,input().split()))[1:])

    for _ in range(m):
        party = set(list(map(int,input().split()))[1:])
        parties.append(party)
        for i in party:
                person[i].update(party)
            
    print(solution(n,parties,known,person))

    '''
    5 4
    1 1
    2 2 3
    2 3 4
    2 4 5
    2 1 5
    답 0
    '''
