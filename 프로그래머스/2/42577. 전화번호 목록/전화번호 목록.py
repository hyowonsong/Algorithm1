# 전화번호 목록

def solution(phone_book):
    # 해시 맵 초기화
    hash_map = {}

    # 각 전화번호의 해시 값을 계산하여 해시 맵에 저장
    for phone_number in phone_book:
        hash_map[phone_number] = True

    # 각 전화번호의 접두어가 해시 맵에 있는지 확인
    for phone_number in phone_book:
        prefix = ""
        for digit in phone_number:
            # prefix라는 변수에 digit을 하나씩 추가하여 접두어 형성            
            prefix += digit      
            
            # 접두어가 해시 맵에 있다면 해당 전화번호는 다른 번호의 접두어
            if prefix != phone_number and prefix in hash_map:
                return False
    
    return True