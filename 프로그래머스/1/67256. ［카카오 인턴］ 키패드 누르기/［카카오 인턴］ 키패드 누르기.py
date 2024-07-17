
def solution(numbers, hand):
    # 키패드 위치를 좌표로 표현
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    
    # 두 위치 사이의 거리를 계산하는 함수
    def distance(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    
    left = keypad['*']  # 왼손 시작 위치
    right = keypad['#']  # 오른손 시작 위치
    answer = ''
    
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            left = keypad[num]
        elif num in [3, 6, 9]:
            answer += 'R'
            right = keypad[num]
        else:
            # 2, 5, 8, 0의 경우
            left_dist = distance(left, keypad[num])
            right_dist = distance(right, keypad[num])
            
            # 중앙 열(2, 5, 8, 0)의 숫자를 누를 때의 로직
            if left_dist < right_dist or (left_dist == right_dist and hand == "left"):
                # 왼손이 더 가깝거나, 
                # 양손 거리가 같은데 왼손잡이인 경우
                answer += 'L'  # 결과 문자열에 'L' 추가
                left = keypad[num]  # 왼손 위치를 현재 숫자의 위치로 업데이트
            else:
                # 오른손이 더 가깝거나,
                # 양손 거리가 같은데 오른손잡이인 경우
                answer += 'R'  # 결과 문자열에 'R' 추가
                right = keypad[num]  # 오른손 위치를 현재 숫자의 위치로 업데이트
    
    return answer