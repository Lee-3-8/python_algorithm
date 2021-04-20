
def solution(item):
    stack = []
    for i in item:
        if i =='(':
            stack.append(i)
        else: # ) 일때
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 'NO'
            
    return 'NO' if stack else 'YES'

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(solution(input()))