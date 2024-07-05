def solution(s):
    dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
                'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    for key,value in dict.items():         # dict.items()는 딕셔너리의 모든 키,값 쌍을 반환
        s = s.replace(key,str(value))
    return int(s)
    