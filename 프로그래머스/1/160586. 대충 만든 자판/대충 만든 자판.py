# 대충 만든 자판

def solution(keymap, targets):
    # 각 문자별 최소 키 누르기 횟수를 저장할 딕셔너리
    min_counts = {}

    # keymap을 순회하면서 각 문자의 최소 키 누르기 횟수를 기록
    for index, word in enumerate(keymap):
        for index_seperate, char in enumerate(word):
            if char not in min_counts:
                # 해당 문자가 나오기까지 필요한 키 누르기 횟수 기록
                min_counts[char] = index_seperate + 1
            else:
                # 기존 기록된 횟수와 현재 횟수 중 최소값 선택
                # "ABACD", "BCEFD"가 keymap에 있고 이미 min_counts에 값이 있다면 둘 중에 더 빨리 문자가 나오는 것은 min_counts에 선택하는 것이다. 
                min_counts[char] = min(min_counts[char], index_seperate + 1)

    # 각 목표 문자열을 작성하기 위해 필요한 최소 키 누르기 횟수를 계산
    result = []
    
    # 각 target 문자열에 대해 반복
    for target in targets:
        answer = 0 # answer 초기화
        
        # target 문자열의 각 문자에 대해 반복
        for char in target:
             # 해당 문자가 자판에 존재하는지 확인
            if char in min_counts:
                # 자판에 존재하면 문자를 입력하기 위한 최소 누르기 횟수 추가
                answer += min_counts[char]
            else:
                # 자판에 존재하지 않으면 문자열 작성이 불가능하므로 -1로 설정
                answer = -1
                # 더 이상 반복할 필요 없이 종료
                break
        result.append(answer)
    
    return result
