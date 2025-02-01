def solution(s):
    answer = []
    
    for word in s.split(" "):  # 공백을 유지 위해 split(" ") 사용
        new_word = ""  # 변환된 단어 저장
        for i, char in enumerate(word):  # 각 단어의 문자별 인덱스 
            # 짝수 번째 -> 대문자
            if i % 2 == 0:
                new_word += char.upper()  
            # 홀수 번째 -> 소문자
            else:
                new_word += char.lower()  
        answer.append(new_word)
    
    # 원래 공백 개수 유지
    return " ".join(answer)  