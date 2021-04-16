
def solution(inp):
    flag = len(inp) // 2

    if len(inp) % 2 == 0: #짝수
        front,back = inp[:flag],inp[flag:]
    else:
        front,back = inp[:flag+1],inp[flag:]

    return 'yes' if front == back[::-1] else 'no'

if __name__ == '__main__':
    inp = ''
    arr = []
    while True:
        inp = input()
        if inp == '0':
            break
        arr.append(inp)
    for i in arr:
        print(solution(i))    


## 대칭이기때문에 거꾸로 뒤집어서 맞는지만 비교해도 된다.