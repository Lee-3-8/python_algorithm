import sys
input = sys.stdin.readline

def solution(stack,cmd,num = None):
    cmd_map = {
        'push': lambda : stack.append(num),
        'pop': lambda : print(stack.pop() if stack else -1),
        'size': lambda : print(len(stack)),
        'empty': lambda : print(0 if stack else 1),
        'top': lambda : print(stack[-1] if stack else -1)
    }

    return cmd_map[cmd]()

if __name__ == '__main__':
    n = int(input())
    stack = []
    for i in range(n):
        cmd = input().split()
        solution(stack,*cmd)