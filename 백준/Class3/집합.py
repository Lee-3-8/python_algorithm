import sys

input = sys.stdin.readline
new_s = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}

def solution(s,cmd, num = 0):

    def all_s():
        s.clear()
        s.update(new_s)

    def check():
        result = 1 if num in s else 0
        print(result)
        return result

    cmd_map = {
        'add': lambda: s.add(num),
        'remove': lambda: s.discard(num),
        'check': check,
        'toggle': lambda: s.remove(num) if num in s else s.add(num),
        'all': all_s,
        'empty': lambda: s.clear(),
    }

    return cmd_map[cmd]()

if __name__ == '__main__':
    n = int(input())
    s = set()
    for i in range(n):
        cmds = input().split()
        solution(s,*cmds)

