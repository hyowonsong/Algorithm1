# 문자열 나누기

def solution(s):
    # 문자열 개수 세기, 현재 인덱스, 문자열 s의 길이 변수 이렇게 3개 필요
    answer = 0
    i = 0
    n = len(s)

    while i<n:
        # 현재 부분 문자열의 첫 번째 문자를 x로 설정
        x = s[i]        
        count_x = 0       
        count_other = 0

        while i<n:

            # 현재 문자가 x인 경우
            if s[i] == x:     
                count_x +=1  

            # 현재 문자가 x가 아닌 경우    
            else:             
                count_other += 1

            # 인덱스를 다음 문자로 이동
            i += 1

            # x와 x가 아닌 문자의 개수가 같은 경우
            if count_x == count_other:
                break
    
        answer += 1
    return answer

