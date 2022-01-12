def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    intersection = lost & reserve
    lost = lost - intersection
    reserve = reserve - intersection

    for i in reserve:
        if i != 1 and i - 1 in lost:
            lost.remove(i - 1)
        elif i != 30 and i + 1 in lost:
            lost.remove(i + 1)
    return n - len(lost)
