
arr = []
for i in range(9):
    n = int(input())
    arr.append(n)

max_n = max(arr)
print(max_n)
print(arr.index(max_n)+1)