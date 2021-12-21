def solution(rows, columns, queries):
    arr = [[(i - 1) * columns + j for j in range(1, columns + 1)]
           for i in range(1, rows + 1)]
    result = []

    def rotate(query):
        s_x, s_y, e_x, e_y = map(lambda x: x-1, query)
        min_v = float("inf")
        temp1 = arr[s_x][s_y]
        for y in range(s_y, e_y):
            temp2 = arr[s_x][y+1]
            min_v = min(temp1, min_v)
            arr[s_x][y+1] = temp1
            temp1 = temp2
        for x in range(s_x, e_x):
            temp2 = arr[x+1][e_y]
            min_v = min(temp1, min_v)
            arr[x+1][e_y] = temp1
            temp1 = temp2
        for y in range(e_y, s_y, -1):
            temp2 = arr[e_x][y-1]
            min_v = min(temp1, min_v)
            arr[e_x][y-1] = temp1
            temp1 = temp2
        for x in range(e_x, s_x, -1):
            temp2 = arr[x-1][s_y]
            min_v = min(temp1, min_v)
            arr[x-1][s_y] = temp1
            temp1 = temp2
        return min_v

    for query in queries:
        result.append(rotate(query))
    return result


if __name__ == "__main__":
    # print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
    # print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
    print(solution(100, 97, [[1, 1, 100, 97]]))
