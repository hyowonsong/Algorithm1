# 문자열 나누기

def solution(s):
    answer = 0  

    # 문자열이 비어 있지 않을 동안 반복
    while s:  
        # 현재 문자열의 첫 번째 글자를 기준으로 설정
        x = s[0]  

        # 기준 글자 x의 개수, 기준 글자가 아닌 글자의 개수를 저장
        count_x = 0  
        count_not_x = 0  
        
        # 문자열의 각 글자를 순회
        for i in range(len(s)):  
            # 현재 글자가 기준 글자와 같다면
            if s[i] == x:  
                count_x += 1  
            # 현재 글자가 기준 글자와 다르다면    
            else:  
                count_not_x += 1  
            
            # 기준 글자와 기준이 아닌 글자의 개수가 같아지면
            if count_x == count_not_x:
                # 분리된 문자열 개수를 증가  
                answer += 1  
                # 현재까지 읽은 문자열을 제거하고 남은 문자열로 갱신
                s = s[i+1:]
                # 현재 반복 종료 후 남은 문자열 처리  
                break  
                
        # for문이 끝날 때까지 두 개수가 같지 않은 경우
        else:  
            # 남은 문자열을 하나의 부분 문자열로 간주
            answer += 1
            # 더 이상 처리할 문자열이 없으므로 작업 종료  
            break  
    
    return answer  
