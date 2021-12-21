import datetime


def solution(a, b):
    input_date = datetime.datetime(2016, a, b)
    return input_date.strftime("%a").upper()


if __name__ == "__main__":
    print(solution(5, 24))
