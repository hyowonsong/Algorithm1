def solution(arr):
    answer = []
    for i in arr:
        if len(answer) == 0:
            answer.append(i)
        else:
            if i == answer[-1]:  # 현재 요소가 answer의 마지막 요소와 같은지 확인
                continue
            else:
                answer.append(i)
    return answer