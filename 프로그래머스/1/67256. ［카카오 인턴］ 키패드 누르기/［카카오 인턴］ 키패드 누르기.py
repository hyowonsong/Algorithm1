# 키패드 누르기

def solution(numbers, hand):
    # 키패드 좌표 매핑
    keypad = {
        1 : (0,0), 2:(0,1), 3:(0,2),
        4 : (1,0), 5:(1,1), 6:(1,2),
        7 : (2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2)
    }
    
    # 초기 위치 설정
    left_pos = keypad['*']
    right_pos = keypad['#']
    
    # 결과 문자열
    result = []
    
    # 손잡이 설정
    if hand == "left":
        hand_preference = "L" 
    else:
        hand_preference = "R"
    
    # 번호 순회
    for num in numbers:
        current = keypad[num]
        
        if num in [1, 4, 7]:  # 왼쪽 열
            result.append("L")
            left_pos = current

        elif num in [3, 6, 9]:  # 오른쪽 열
            result.append("R")
            right_pos = current

        else:  # 가운데 열
            # 거리 계산(맨하튼 거리 사용)
            left_distance = abs(left_pos[0] - current[0]) + abs(left_pos[1] - current[1])
            right_distance = abs(right_pos[0] - current[0]) + abs(right_pos[1] - current[1])
            
            # 왼손이 더 가까움
            if left_distance < right_distance:  
                result.append("L")
                left_pos = current
            # 오른손이 더 가까움
            elif left_distance > right_distance:  
                result.append("R")
                right_pos = current
            # 거리가 같음
            else:  
                result.append(hand_preference)
                if hand_preference == "L":
                    left_pos = current
                else:
                    right_pos = current
    
    return "".join(result)