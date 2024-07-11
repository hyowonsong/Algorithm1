def solution(order):
    stack = []  
    current_box = 1  # 현재 처리 중인 메인 컨테이너 벨트의 상자 번호
    loaded = 0  # 트럭에 실은 상자의 수
    
    for next_box in order:  # order 리스트를 순회
        # 현재 상자가 필요한 상자보다 작은 경우, 그 사이의 모든 상자를 스택에 추가
        while current_box < next_box:
            stack.append(current_box)
            current_box += 1
        
        if current_box == next_box:  # 현재 상자가 필요한 상자인 경우
            loaded += 1  # 트럭에 실음
            current_box += 1  # 다음 상자로 이동

        elif stack and stack[-1] == next_box:  # 스택의 맨 위 상자가 필요한 상자인 경우
            stack.pop()  # 스택에서 상자를 꺼냄
            loaded += 1  # 트럭에 실음
            
        else:  # 위의 조건을 모두 만족하지 않으면 더 이상 상자를 싣지 못함
            break  # 반복 중단
    
    return loaded  # 트럭에 실은 총 상자 수 반환