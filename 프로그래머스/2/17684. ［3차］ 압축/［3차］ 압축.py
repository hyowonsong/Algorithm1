# 3차 압축

def solution(msg):
    # 1. 길이가 1인 모든 단어(A-Z)를 포함하도록 사전을 초기화
    # ASCII 코드를 이용해 A=1, B=2, ..., Z=26으로 매핑
    dictionary = {chr(65+i): i+1 for i in range(26)}
    
    # 압축 결과를 저장할 리스트
    answer = []
    # 현재 처리 중인 문자열
    w = ""
    # 다음에 사전에 추가될 단어의 색인 번호 (A-Z는 이미 1-26이므로 27부터 시작)
    next_index = 27
    
    # 입력 문자열의 각 문자에 대해 반복
    for c in msg:
        # 현재 처리 중인 문자열(w)에 새 문자(c)를 추가
        wc = w + c
        
        # 만약 wc가 이미 사전에 있다면
        if wc in dictionary:
            # w를 업데이트하고 다음 문자로 넘어감
            w = wc
        else:
            # 2,3. 현재 입력과 일치하는 가장 긴 문자열(w)의 색인 번호를 출력
            answer.append(dictionary[w])
            
            # 4. 새로운 단어(wc)를 사전에 추가
            dictionary[wc] = next_index
            # 다음 색인 번호 준비
            next_index += 1
            
            # w를 현재 문자(c)로 초기화
            w = c
    
    # 마지막 남은 단어 처리
    # 모든 문자를 처리한 후에도 w에 처리되지 않은 문자열이 남아있을 수 있음
    if w:
        answer.append(dictionary[w])
    
    # 압축된 색인 번호 리스트 반환
    return answer

