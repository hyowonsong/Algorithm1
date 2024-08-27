from collections import Counter

def solution(X, Y):
    # 각 숫자의 빈도를 카운트
    count_x = Counter(X)
    count_y = Counter(Y)
    
    # 공통 숫자들을 저장할 리스트
    common_digits = []
    
    # 0부터 9까지 숫자를 확인하며 공통된 숫자를 찾음
    for digit in range(10):
        digit = str(digit)
        if digit in count_x and digit in count_y:
            # 두 수에서 공통으로 나타나는 숫자 중 최소 빈도만큼만 사용
            common_count = min(count_x[digit], count_y[digit])
            common_digits.extend([digit] * common_count)
    
    # 공통된 숫자가 없으면 -1 반환
    if not common_digits:
        return "-1"
    
    # 공통된 숫자를 내림차순으로 정렬하여 큰 숫자를 만듦
    common_digits.sort(reverse=True)
    
    # 결과가 '0'으로만 구성되어 있으면 '0' 반환
    if common_digits[0] == '0':
        return "0"
    
    return "".join(common_digits)