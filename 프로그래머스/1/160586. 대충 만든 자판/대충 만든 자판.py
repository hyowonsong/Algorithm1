# 대충 만든 자판
def solution(keymap, targets):
    # 각 문자별 최소 키 누르기 횟수를 저장할 딕셔너리
    min_counts = {}
    
    # keymap을 순회하면서 각 문자의 최소 키 누르기 횟수를 기록
    for index, values in enumerate(keymap):
        for index_count, char in enumerate(values):
            if char not in min_counts:
                # 해당 문자가 나오기까지 필요한 키 누르기 횟수 기록
                min_counts[char] = index_count + 1  
            else:
                # 기존 기록된 횟수와 현재 횟수 중 최소값 선택
                min_counts[char] = min(min_counts[char], index_count + 1)  


    # 각 목표 문자열을 작성하기 위해 필요한 최소 키 누르기 횟수를 계산
    result = []
    
    # 각 target 문자열에 대해 반복
    for target in targets:
        total = 0
        
        # target 문자열의 각 문자에 대해 반복
        for char in target:
             # 해당 문자가 자판에 존재하는지 확인
            if char in min_counts:
                # 자판에 존재하면 문자를 입력하기 위한 최소 누르기 횟수 추가
                total += min_counts[char]
            else:
                # 자판에 존재하지 않으면 문자열 작성이 불가능하므로 -1로 설정
                total = -1
                # 더 이상 반복할 필요 없이 종료
                break
        result.append(total)
    
    return result