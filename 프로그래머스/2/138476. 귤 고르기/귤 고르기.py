def solution(k, tangerine):
    # 귤 크기의 빈도를 저장할 딕셔너리
    dict = {}
    for i in tangerine:
        # 만약 딕셔너리에 i 가 있다면 +=1 
        if i in dict:
            dict[i] += 1
        # 만약 딕셔너리에 없다면 = 1 로 설정해주기
        else:
            dict[i] = 1
    
    # 빈도를 리스트로 변환한 후 빈도순으로 정렬
    # sort 메서드는 리스트를 직접 정렬하는 반면, 
    # sorted() 함수는 정렬된 새로운 리스트를 반환하며,원본 리스트는 변경X
    dict_list = sorted(dict.values(), reverse=True)
    
    total = 0
    answer = 0
    
    # 빈도가 높은 순서대로 귤을 선택(values 값만 가져옴)
    for i in dict_list:
        total += i
        answer += 1
        # 수확한 귤 판매하는 것보다 total이 많으면 break
        if total >= k:
            break
    
    return answer
