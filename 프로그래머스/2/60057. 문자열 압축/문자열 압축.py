def solution(s):
    # 문자열 길이가 1인 경우 바로 1 반환
    if len(s) == 1:
        return 1
    
    # 가능한 모든 압축 결과 중 최소 길이를 저장
    min_length = len(s)
    
    # 1부터 문자열 길이의 절반까지 모든 가능한 단위로 시도
    for unit in range(1, len(s) // 2 + 1):
        compressed = ""
        count = 1
        prev = s[0:unit]
        
        # unit 크기만큼 문자열을 순회하며 압축
        for i in range(unit, len(s), unit):
            # 현재 단위만큼의 문자열 추출
            curr = s[i:i + unit]
            
            # 이전 문자열과 같다면 count 증가
            if prev == curr:
                count += 1
            # 다르다면 압축 결과에 추가하고 초기화
            else:
                if count > 1:
                    compressed += str(count)
                compressed += prev
                prev = curr
                count = 1
        
        # 마지막 문자열 처리
        if count > 1:
            compressed += str(count)
        compressed += prev
        
        # 최소 길이 갱신
        min_length = min(min_length, len(compressed))
    
    return min_length