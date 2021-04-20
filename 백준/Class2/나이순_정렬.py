
if __name__ == '__main__':
    t = int(input())
    arr = []
    for i in range(t):
        age, name = input().split()
        arr.append((int(age),i,name))
    for i in sorted(arr):
        print(i[0],i[2])
    