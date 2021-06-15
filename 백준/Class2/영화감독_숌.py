
def solution(n):
    cur = 0
    num = 665
    while cur != n:
        num += 1
        if '666' in str(num):
            cur += 1
    return num

if __name__ == '__main__':
    n = int(input())
    print(solution(n))