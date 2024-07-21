def solution(numbers):
    # 숫자들을 문자열로 변환
    numbers = list(map(str, numbers))
    
    # 숫자를 이어 붙였을 때 큰 순서대로 정렬
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    # 정렬된 숫자들을 이어 붙여 결과 생성
    answer = ''.join(numbers)
    
    # 모든 숫자가 0일 경우 '0'을 반환
    return '0' if answer[0] == '0' else answer