def solution(s):
    answer = ''
    # 문자열을 공백을 기준으로 분할하여 리스트로 변환
    s = s.split(' ')
    # 리스트의 각 단어에 대해 반복
    for i in s:
        for j in range(len(i)):
            # 인덱스가 짝수인 경우
            if j % 2 == 0:
                answer += i[j].upper()
            # 인덱스가 짝수가 아닌 경우
            else:
                answer += i[j].lower()
        # 각 단어 처리 후에 공백 추가
        answer +=' '
    # 마지막 단어 이후의 불필요한 공백 제거 후 반환
    return answer[:-1]