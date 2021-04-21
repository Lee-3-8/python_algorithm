import sys
input = sys.stdin.readline

# if __name__ == '__main__':
#     n = int(input())
#     dic = {}
#     for i in range(n):
#         num = int(input())
#         dic[num] = dic.get(num,0) + 1
#     for i in sorted(dic.items(),key=lambda x:x[0]):
#         for _ in range(i[1]):
#             print(i[0])
## 10492ms

# import sys
# input = sys.stdin.readline

# if __name__ == '__main__':
#     n = int(input())
#     arr = [0]*10001
#     for i in range(n):
#         arr[int(input())]+=1
#     for i,v in enumerate(arr):
#         for _ in range(v):
#             print(i)
# 8512ms