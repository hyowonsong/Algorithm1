# 영어 끝말잇기

# 1. 1번부터 번호 순서대로 단어를 말합니다.
# 2. 마지막 사람이 단어를 말한 다음에는 다시 1번부터 시작합니다.
# 3. 앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
# 4. 이전에 등장했던 단어는 사용할 수 없습니다.
# 5. 한 글자인 단어는 인정되지 않습니다.

# 가장 먼저 탈락하는 사람의 번호와 그 사람이 몇 번째 차례에 탈락하는지 구하기

def solution(n, words):
    last_words = [] 

    for idx, word in enumerate(words):
        if idx > 0:  # 첫 번째 단어는 검사를 생략
            # 앞 단어의 끝 글자와 현재 단어의 첫 글자가 다르거나, 이미 말한 단어를 다시 말한 경우
            if words[idx - 1][-1] != word[0] or word in last_words:
                # 탈락자 번호와 차례 계산
                person = (idx % n) + 1
                turn = (idx // n) + 1
                return [person, turn]

        last_words.append(word)  # 단어를 기록

    return [0, 0]  # 탈락자가 없으면 [0, 0] 반환

