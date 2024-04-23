# 해시맵으로 구현 -> 공간을 배열보다 많이 배정해서 찾는 시간을 줄이자

def solution(phone_book): 
    # 1. Hash map 생성
    hash_map = {}
    for nums in phone_book:
        hash_map[nums] = 1
    
    # 2. 접두어가 Hash map에 존재하는지 찾기
    for nums in phone_book:
        arr = ""
        for num in nums:
            arr+=num
            
            # 3. 본인 자체인 경우는 제외
            if arr in hash_map and arr != nums:
                return False
    return True