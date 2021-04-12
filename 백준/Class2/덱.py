from collections import deque
import sys

def solution(cmd, x = None):
    cmd_map = {
        'push_front': lambda x: deq.appendleft(int(x)),
        'push_back': lambda x: deq.append(int(x))
    }
    cmd_map2 = {
        'pop_front': lambda : deq.popleft() if len(deq) != 0 else -1,
        'pop_back': lambda : deq.pop() if len(deq) != 0 else -1,
        'size' : lambda : len(deq),
        'empty': lambda : 1 if len(deq) == 0 else 0,
        'front': lambda :deq[0] if len(deq) != 0 else -1,
        'back': lambda :deq[-1] if len(deq) != 0 else -1
    }
    if x != None:
        cmd_map[cmd](x)
    else:
        print(cmd_map2[cmd]())
    return

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    deq = deque()
    for i in range(n):
        cmd = sys.stdin.readline().split()
        solution(*cmd)
