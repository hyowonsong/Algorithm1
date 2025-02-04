# n진수 게임

# n진법 변환 함수
def convert_to_base(number, base):
    # number가 0인 경우
    if number == 0:
        return "0"
    
    # number가 0이 아닌 경우
    digits = []
    while number > 0:       # 0보다 클 때까지 계속해서 진법 변환
        remainder = number % base
        if remainder < 10:
            digits.append(str(remainder))
        # 10보다 크면 변환해줘야 한다. chr는 숫자를 문자로 반환해준다.  
        else:
            digits.append(chr(remainder-10+ord('A'))) # 10~15 -> A~F
            
        # number를 갱신해 다음 자리 숫자 계산.
        number //= base
        
    #진법 맨 마지막에 있는 것을 맨 처음 계산했기 때문에 반드시 역순반환!(중요)
    return digits[::-1]  

def solution(n, t, m, p):
    # 모든 숫자를 담을 리스트
    sequence = []
    #number는 모든 숫자를 하나씩 돌아가면서 진법 변환할 수 있게 해준다.(중요!)
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
    return "".join(lst)