import sys

def solution(n_dic,m_arr):
    for i in m_arr:
        print (1 if i in n_dic else 0)

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    n_dic = {i:i for i in sys.stdin.readline().split()}
    m = int(sys.stdin.readline())
    m_arr = sys.stdin.readline().split()
    solution(n_dic,m_arr)

    # dict 보다 set이 더 나았을 것 같다. 출력을 모아서하면 성능향상에 도움이된다.