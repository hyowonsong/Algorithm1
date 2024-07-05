# 문자열 내 마음대로 정렬하기
# 각 문자열 n 번째 인덱스를 기준으로 오름차순 정렬

def solution(strings, n):
    answer = []
    new_answer = []
    strings.sort()    # 문자열 정리

    for i in strings:
        new_answer.append(i[n])     # 문자열의 n번째 단어만 append
        new_answer.sort()           # new_answer 정리
    for i in new_answer:
        for string in strings:        # string 돌면서 n번째 문자열이 i 이고 answer에 없다면 
            if string[n] == i and string not in answer:      
                answer.append(string)
    return answer