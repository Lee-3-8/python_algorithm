
if __name__ == '__main__':
    n = int(input())
    arr = set()
    for i in range(n):
        inp = input()
        arr.add(inp)
    arr = sorted(arr,key=lambda x: (len(x),x))
    for i in arr:
        print(i)