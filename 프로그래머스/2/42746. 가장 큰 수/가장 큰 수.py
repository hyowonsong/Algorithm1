from functools import cmp_to_key

def compare(a, b):
    # a+b와 b+a를 직접 비교
    # 음수를 반환하면 첫 번째 인자가 두 번째 인자보다 "작다"고 판단
    # 양수를 반환하면 첫 번째 인자가 두 번째 인자보다 "크다"고 판단
    if a + b > b + a:
        # a+b가 더 크면 a가 앞에 와야 함
        # -1을 반환하여 a가 b보다 앞에 오도록 함
        return -1
    elif a + b < b + a:
        # b+a가 더 크면 b가 앞에 와야 함
        # 1을 반환하여 b가 a보다 앞에 오도록 함
        return 1
    else:
        # a+b와 b+a가 같으면 순서가 상관없음
        return 0

def solution(numbers):
    
    # 숫자들을 문자열로 변환
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))
    
    # 정렬된 숫자들을 이어 붙여 결과 생성
    answer = ''.join(numbers)
    
    # 모든 숫자가 0일 경우 '0'을 반환
    # 그렇지 않으면 생성된 문자열을 그대로 반환
    if answer[0] == '0':
        return '0'  
    else:
        return answer