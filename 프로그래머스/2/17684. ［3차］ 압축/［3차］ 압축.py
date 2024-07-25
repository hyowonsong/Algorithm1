def solution(msg):
    # 1. 길이가 1인 모든 단어(A-Z)를 포함하도록 사전을 초기화
    # 'A'부터 'Z'까지 각 문자에 대해 색인 번호를 부여
    # char(65) 는 A를 의미
    dictionary = {}
    for i in range(26):
        dictionary[chr(65 + i)] = i + 1
    
    # 압축 결과를 저장할 리스트
    answer = []
    
    # 현재까지 확인된 가장 긴 문자열
    current_string = ''
    # 다음에 사전에 추가될 단어의 색인 번호 (A-Z는 이미 1-26이므로 27부터 시작)
    next_index = 27
    
    # 입력 문자열의 각 문자에 대해 반복
    for char in msg:
        # 현재 문자열(current_string)에 새 문자(char)를 추가한 새로운 문자열
        new_string = current_string + char
        
        # 만약 새로운 문자열(new_string)이 이미 사전에 있다면
        if new_string in dictionary:
            # current_string을 새로운 문자열로 업데이트하고 계속 진행
            current_string = new_string
        else:
            # 2,3. 현재 문자열과 일치하는 가장 긴 문자열(current_string)의 색인 번호를 출력
            answer.append(dictionary[current_string])
            
            # 4. 새로운 문자열(new_string)을 사전에 추가
            dictionary[new_string] = next_index
            # 다음 색인 번호 준비
            next_index += 1
            
            # current_string을 새 문자(char)로 초기화
            current_string = char
    
    # 마지막 남은 단어 처리
    # 모든 문자를 처리한 후에도 current_string에 처리되지 않은 문자열이 남아있을 수 있음
    if current_string:
        answer.append(dictionary[current_string])
    
    # 압축된 색인 번호 리스트 반환
    return answer
