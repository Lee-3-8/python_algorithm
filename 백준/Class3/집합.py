import sys

input = sys.stdin.readline

# def solution(s,cmd, num = 0):
#     def all_s():
#         s.clear()
#         s.update({1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20})
#         return

#     def check():
#         result = 1 if int(num) in s else 0
#         print(result)
#         return result

#     cmd_map = {
#         'add': lambda: s.add(int(num)),
#         'remove': lambda: s.discard(int(num)),
#         'check': check,
#         'toggle': lambda: s.remove(int(num)) if int(num) in s else s.add(int(num)),
#         'all': all_s,
#         'empty': lambda: s.clear(),
#     }

#     return cmd_map[cmd]()

def solution(s,cmd, num = 0):

    def all_s():
        s.clear()
        s.update({1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20})

    def check():
        result = 1 if int(num) in s else 0
        print(result)
        return result

    num = int(num)
    if cmd == 'add': s.add(num)
    elif cmd == 'remove': s.discard(num)
    elif cmd == 'check': check()
    elif cmd == 'toggle': s.remove(num) if num in s else s.add(num)
    elif cmd == 'all': all_s()
    elif cmd == 'empty': s.clear()

if __name__ == '__main__':
    n = int(input())
    s = set()
    for i in range(n):
        cmds = input().split()
        solution(s,*cmds)

