def solution(n, words):
    used_words = []
    used_words.append(words[0])
    last_words = words[0][-1]
    number, order = 0, 0              # 여기 0, 0 이어야 된다.
    
    for i in range(1,len(words)):      # 맨 처음에 0은 위에서 지정해줬으니 1부터
        if words[i] not in used_words and words[i][0] == last_words:
            used_words.append(words[i])
            last_words = words[i][-1]
        else:
            number = (i%n) + 1
            order = (i//n) +1
            break
            
    return [number, order]