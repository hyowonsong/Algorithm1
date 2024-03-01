# 명예의 전당(1)

def solution(k, score):
    answer = []  
    number = []  
    
    for i in score:                   # score 리스트의 각 원소에 대해 반복
        if len(number) < k:      # 현재 그룹의 크기가 k보다 작을 경우 해당 원소 추가
            number.append(i)       
        else:                        # 현재 그룹의 크기가 k와 같거나 큰 경우
            if min(number) < i: # 현재 원소가 현재 그룹의 최소값보다 큰 경우 최솟갑 제거
                number.remove(min(number))    
                number.append(i)          # 현재 원소를 현재 그룹에 추가
        answer.append(min(number))        # 현재 그룹의 최소값을 answer 리스트에 추가

    return answer                   # 모든 그룹의 최소값을 담은 리스트를 반환