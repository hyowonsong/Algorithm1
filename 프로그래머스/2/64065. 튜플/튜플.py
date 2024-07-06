def solution(s):
    # 문자열에서 집합을 추출
    sets = s[2:-2].split('},{')
    
    # 각 집합을 리스트로 변환하고, 길이 순으로 정렬
    sets = [set(map(int, x.split(','))) for x in sets]
    sets.sort(key=len)
    
    answer = []
    for subset in sets:
        # 집합에서 아직 추가되지 않은 원소를 찾아서 추가
        for num in subset:
            if num not in answer:
                answer.append(num)
                break
    
    return answer
