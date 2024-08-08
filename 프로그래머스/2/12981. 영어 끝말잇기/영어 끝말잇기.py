def solution(n, words):
    used_words = []
    used_words.append(words[0])
    last_words = words[0][-1]
    number, order = 0, 0              # 여기 0, 0 이어야 된다.
    
    # 맨 처음에 0은 위에서 지정해줬으니 1부터
    for i in range(1,len(words)):    
        # words[i] 가 used_words에 없고 
        # words[i]의 첫 글자가 last_words 라면
        if words[i] not in used_words and words[i][0] == last_words:
            used_words.append(words[i])
            last_words = words[i][-1]
        else:
            # 현재 차례에 단어를 말한 사람의 번호
            number = (i%n) + 1
            # 현재 차례의 순서를 나타냅니다.
            order = (i//n) +1
            break
            
    return [number, order]