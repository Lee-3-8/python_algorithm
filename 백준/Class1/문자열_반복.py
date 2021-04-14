n = int(input())
for i in range(n):
    r,st = input().split()
    new_s = ''
    for i in st:
        new_s += i*int(r)
    print(new_s)