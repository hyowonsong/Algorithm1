def solution(phone_book):
    phone_book.sort()
    
    # 정렬된 전화번호부를 순회하면서 인접한 두 번호끼리 접두어 관계인지 확인
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    
    return True
