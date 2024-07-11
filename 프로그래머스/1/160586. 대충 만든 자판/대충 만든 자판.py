# 대충 만든 자판

def solution(keymap, targets):
    # 각 문자별 최소 키 누르기 횟수를 저장할 딕셔너리
    min_counts = {}
    
    # keymap을 순회하면서 각 문자의 최소 키 누르기 횟수를 기록
    for key_index, keys in enumerate(keymap):
        for press_count, char in enumerate(keys):
            if char not in min_counts:
                # 해당 문자가 나오기까지 필요한 키 누르기 횟수 기록
                min_counts[char] = press_count + 1  
            else:
                # 기존 기록된 횟수와 현재 횟수 중 최소값 선택
                min_counts[char] = min(min_counts[char], press_count + 1)  


    # 각 목표 문자열을 작성하기 위해 필요한 최소 키 누르기 횟수를 계산
    result = []
    for target in targets:
        total = 0
        for char in target:
            if char in min_counts:
                total += min_counts[char]
            else:
                total = -1
                break
        result.append(total)
    
    return result