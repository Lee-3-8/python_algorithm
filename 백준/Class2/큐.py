import sys
from collections import deque
input = sys.stdin.readline

def solution(que,cmd,num = None):
    cmd_map = {
        'push': lambda : que.append(num),
        'pop': lambda : print(que.popleft() if que else -1),
        'size': lambda : print(len(que)),
        'empty': lambda : print(0 if que else 1),
        'front': lambda : print(que[0] if que else -1),
        'back': lambda : print(que[-1] if que else -1)
    }

    return cmd_map[cmd]()

if __name__ == '__main__':
    n = int(input())
    que = deque()
    for i in range(n):
        cmd = input().split()
        solution(que,*cmd)