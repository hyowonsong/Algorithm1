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
        if num in [1, 4, 7]:  # 왼쪽 열
            result.append("L")
            left_pos = keypad[num]  # 현재 위치 변경

        elif num in [3, 6, 9]:  # 오른쪽 열
            result.append("R")
            right_pos = keypad[num] # 현재 위치 변경

        else:  # 가운데 열
            # 거리 계산(맨해튼 거리 사용)
            left_distance = abs(left_pos[0] - keypad[num][0]) + abs(left_pos[1] - keypad[num][1])
            right_distance = abs(right_pos[0] - keypad[num][0]) + abs(right_pos[1] - keypad[num][1])
            
            if left_distance < right_distance:  # 왼손이 더 가까움
                result.append("L")
                left_pos = keypad[num]
                
            elif left_distance > right_distance:  # 오른손이 더 가까움
                result.append("R")
                right_pos = keypad[num]
                
            else:  # 거리가 같으면 자신의 선호 선을 기준
                result.append(hand_preference)
                if hand_preference == "L":
                    left_pos = keypad[num]
                else:
                    right_pos = keypad[num]
    
    return "".join(result)