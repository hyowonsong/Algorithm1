def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]

    answer = 0

    for bab in babbling:
        for pw in words:
            # 같은 발음이 연속되는 경우는 제외
            if pw*2 in bab:
                break
            else:
                # 가능한 발음들을 반복하여 단어에서 제거
                bab = bab.replace(pw, " ")

        # 문자열이 비어 있으면 유효한 발음
        if bab.isspace():
            answer += 1

    return answer