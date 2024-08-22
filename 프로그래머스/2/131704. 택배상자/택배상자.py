def solution(order):
    assist = []  
    answer = 0  
    cur = 1  # 현재 메인 컨테이너 벨트에서 처리할 상자 번호

    # order 리스트의 각 상자 번호에 대해 반복
    for box in order:  
        # 현재 상자가 처리할 상자 번호보다 크다면, 보조 벨트로 옮김
        while cur < box:
            assist.append(cur)
            cur += 1
        
        # 현재 상자가 필요한 상자와 일치하면 
        # 트럭에 싣고 카운트 증가 및 다음 상자로 이동
        if cur == box:  
            answer += 1  
            cur += 1  
        # 보조 벨트 맨 위 상자가 필요한 상자라면
        elif assist and assist[-1] == box:  
            assist.pop()  
            answer += 1  
        # 위 조건들에 해당하지 않으면 (즉, 필요한 상자를 찾을 수 없으면)
        # 더 이상 진행 불가능하므로 반복 중단
        else:  
            break 

    return answer  