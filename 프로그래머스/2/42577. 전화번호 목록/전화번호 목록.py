# 전화번호 목록

def solution(phone_book):
    dict = {}

    # 각 전화번호의 해시 값을 계산하여 해시 맵에 저장(여기 저장하는게 중요)
    for i in phone_book:
        dict[i] = True

    # 각 전화번호의 접두어가 해시 맵에 있는지 확인
    for i in phone_book:
        prefix = ""
        for digit in i:
            # prefix라는 변수에 digit을 하나씩 추가하여 접두어 형성         
            prefix += digit      
            
            # 접두어가 해시 맵에 있다면 해당 전화번호는 다른 번호의 접두어
            # 자기 자신을 접두어로 판단하지 않기 위해 i는 빼고 체크
            if prefix != i and prefix in dict:
                return False
    
    return True