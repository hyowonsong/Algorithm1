def solution(babbling):
    # 발음 가능한 단어 목록
    possible_words = ["aya", "ye", "woo", "ma"]
    
    # 발음할 수 있는 단어의 개수
    count = 0
    
    for word in babbling:
        # 연속 발음을 방지하기 위해 같은 발음이 연속으로 있는지 확인
        for pw in possible_words:
            if pw * 2 in word:
                break
        else:
            # 가능한 발음들을 반복하여 단어에서 제거
            for pw in possible_words:
                word = word.replace(pw, " ")
            
            # 모든 가능한 발음이 제거된 후에 남는 글자가 없어야 정상 발음 가능
            if word.strip() == "":
                count += 1
    
    return count