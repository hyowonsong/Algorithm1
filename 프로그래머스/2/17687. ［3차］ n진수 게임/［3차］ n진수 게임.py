# 숫자를 0부터 시작해서 차례대로 말한다. (0~9)
# 10 이상 부터는 하나씩 끊어서 (1,0) (1,1) (1,2) (1,3)

# 코딩 동아리 일원들은 이진수로 게임을 한다.

# number를 지정된 진법 base로 변환
def convert_to_n(number, base):
    # 0은 모든 진법에서 '0'이므로 0인경우 바로 '0' 반환
    if number == 0:
        return '0'
    # 0~15까지의 숫자를 표현하는 문자열 
    digits = '0123456789ABCDEF'
    
    # 변환 결과를 저장할 빈 문자열 초기화
    result = ''
    while number: 
        # 숫자를 특정 진법으로 변환
        result = digits[number % base] + result
        # 0 이 되는 순간 while 조건 거짓이라 끝남.
        number //= base
    return result

def solution(n, t, m, p):
    # 결과 문자열, 시작 숫자, 전체 게임 시퀀스를 초기화합니다.
    answer = ''
    number = 0
    game_sequence = ''
    
    # 필요한 길이(t * m)가 될 때까지 숫자를 변환하여 시퀀스에 추가
    while len(game_sequence) < t * m:
        game_sequence += convert_to_n(number, n)
        number += 1
    
    # 튜브의 순서에 해당하는 숫자들만 선택하여 결과 문자열에 추가합니다
    for i in range(p-1, t*m, m):
        answer += game_sequence[i]
    
    return answer