
def solution(n):
    fibo = [-1]*21
    fibo[0] = 0
    fibo[1] = 1
    
    def fibonacci(num):
        if fibo[num] != -1:
            return fibo[num]
        fibo[num] = fibonacci(num-1) + fibonacci(num-2)
        return fibo[num]

    return fibonacci(n)

if __name__ == '__main__':
    n = int(input())
    print(solution(n))