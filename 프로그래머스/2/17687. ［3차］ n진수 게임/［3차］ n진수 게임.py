# n진수 게임

def solution(n, t, m, p):
    # 모든 숫자를 담을 리스트
    sequence = []
    number = 0

    # t * m개의 문자가 만들어질 때까지 반복
    # 게임 참가자가 m명이고 튜브가 말해야할 것이 t개이니까 t*m
    while len(sequence) < t * m:
        # 현재 숫자를 n진법으로 변환
        sequence.extend(convert_to_base(number, n))
        number += 1

    # 튜브가 말해야 하는 문자만 선택
    lst = []

    # 튜브의 순서(p)에 해당하는 문자를 m 간격으로 선택
    for i in range(p - 1, len(sequence), m):
        lst.append(sequence[i])

    # 선택된 숫자 중에서 t개만 사용
    lst = lst[:t]

    # 리스트를 문자열로 변환
    result = "".join(lst)
    return result 


# n진법 변환 함수
def convert_to_base(number, base):
    if number == 0:
        return "0"
    
    digits = []
    while number > 0:
        remainder = number % base
        if remainder < 10:
            digits.append(str(remainder))
        # 10보다 크면 변환해줘야 한다.     
        else:
            digits.append(chr(remainder - 10 + ord('A')))  # 10~15 -> A~F
            
        # number를 갱신해 다음 자리 숫자 계산.
        number //= base
    return digits[::-1]  # 역순으로 반환