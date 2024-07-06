def solution(k, tangerine):
    # 귤 크기의 빈도를 저장할 딕셔너리
    freq = {}
    for i in tangerine:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    # 빈도를 리스트로 변환한 후 빈도순으로 정렬
    # sort 메서드는 리스트를 직접 정렬하는 반면, 
    # sorted() 함수는 정렬된 새로운 리스트를 반환하며, 원본 리스트는 변경X
    freq_list = sorted(freq.values(), reverse=True)
    
    total = 0
    kinds = 0
    
    # 빈도가 높은 순서대로 귤을 선택
    for count in freq_list:
        total += count
        kinds += 1
        if total >= k:
            break
    
    return kinds