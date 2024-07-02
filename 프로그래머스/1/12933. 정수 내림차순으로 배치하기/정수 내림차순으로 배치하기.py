def solution(n):
    answer = ''

    n_list = list(str(n))
    n_list.sort(reverse=True)
    # 8,7,3,2,1,1

    for i in n_list:
        answer += i
    return int(answer)