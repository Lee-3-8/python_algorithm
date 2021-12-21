def solution(lottos, win_nums):
    zero_cnt = 0
    min_cnt = 0
    rank = [6, 6, 5, 4, 3, 2, 1]
    for num in lottos:
        if num == 0:
            zero_cnt += 1
        elif num in win_nums:
            min_cnt += 1

    return [rank[min_cnt+zero_cnt], rank[min_cnt]]


if __name__ == "__main__":
    print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
