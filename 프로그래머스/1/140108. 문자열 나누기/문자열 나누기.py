def solution(s):
    result = 0  
    while s:  
        dict = {}
        x = s[0]  # 첫 번째 문자를 x로 지정
        x_count = 0  # x의 등장 횟수
        other_count = 0  # x가 아닌 다른 문자들의 총 등장 횟수
        
        for i, char in enumerate(s):
            if char == x:
                x_count += 1  # x와 같은 문자면 x_count 증가
            else:
                other_count += 1  # x가 아닌 문자면 other_count 증가
                # x가 아닌 문자의 개수를 딕셔너리에 저장 
                dict[char] = dict.get(char, 0) + 1
            
            # x의 개수와 다른 문자들의 총 개수가 같아지면
            if x_count == sum(dict.values()):
                result += 1  # 분해된 문자열 개수 증가
                s = s[i+1:]  # 분해한 부분을 제외한 나머지 문자열로 s 업데이트
                break  # 내부 for 루프 종료
        else:
            # for 루프가 break 없이 끝났다면 (즉, 끝까지 같아지지 않았다면)
            result += 1  # 남은 전체를 하나의 문자열로 취급
            break  # while 루프 종료
    
    return result  # 최종적으로 분해된 문자열의 개수 반환