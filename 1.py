a = int(input())
b = int(input())
n1 = a + b
n2 = a * b

if n1 > n2:
    print("Result =",n1 - n2)
    if n1 - n2 < 8:
        a, b = b, a
        print("Swap!!")
else:
    print("Result =",n2 - n1)
    if n2 - n1 < 8:
        a, b = b, a
        print("Swap!!")

### end조건으로 개행을 없애는 방법###
# print("a =",a,end=', ')
# print("b =",b)
### (추천) 학교에서 주로 가르치는방법 ###
# print("a = %d, b = %d"%(a,b))
### 제가 주로쓰는 방법
# print(f'a = {a}, b = {b}') # use fstring



a = int(input())
b = int(input())
big = a * b
small = a + b

if small > big:
    big,small = small,big

print("Result =",big - small)

if big - small < 8:
    a, b = b, a
    print("Swap!!")

print("a = %d, b = %d"%(a,b))