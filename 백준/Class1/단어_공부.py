from collections import Counter

def solution(string):
    dic = Counter(string.upper())
    v_max = max(dic.values())
    result = []
    for i in dic:
        if dic[i] == v_max:
            result.append(i)
    return '?' if len(result) > 1 else result[0]

if __name__ == '__main__':
    a = input()
    print(solution(a))