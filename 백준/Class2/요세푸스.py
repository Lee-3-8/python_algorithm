
def main():
    n,m = map(int,input().split())
    arr = [i for i in range(1,n+1)]
    result = []
    index = m -1

    while True:
        result.append(arr.pop(index))
        if not arr: break;
        index = (index + m - 1) % (len(arr))

    print(f'<{result[0]}',end='')
    for i in result[1: ]:
        print(f', {i}',end='')
    print(">")
    return
    
if __name__=="__main__":
    main()