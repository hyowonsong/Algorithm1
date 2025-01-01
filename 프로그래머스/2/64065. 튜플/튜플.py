def solution(s):
    # 문자열에서 양 끝의 '{{'와 '}}' 제거, 문자열을 '},{'로 분리
    s = s[2:-2].split('},{')

    # 각 집합을 문자열에서 정수 리스트로 변환
    lst = []
    for group in s:
        # 쉼표(,)를 기준으로 나눕니다.
        numbers = group.split(',')
        # 쉼표를 기준으로 나눈 것을 다시 리스트로 변환합니다. 
        lst.append(list(map(int, numbers)))

    
    # 집합을 길이에 따라 정렬
    lst.sort(key = len)
    
    # 결과 튜플을 담을 리스트
    answer = []
    for group in lst:
        for num in group:
            if num not in answer:
                answer.append(num)
                break

    return answer
    