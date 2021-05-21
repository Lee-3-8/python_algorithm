from collections import Counter
A = int(input())
B = int(input())
C = int(input())

dic = Counter(str(A*B*C))
for i in range(9+1):
    print(dic.get(str(i),0))