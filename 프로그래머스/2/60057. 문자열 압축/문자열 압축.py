def solution(s):
    answer = len(s)
    # 1개 단위부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s)//2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        # 단위 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수 증가
            if prev == s[j:j+step]:
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하면)
            else:
                if count >= 2:
                    compressed += str(count) + prev 
                else:
                    compressed += prev  # 수정: 반복이 없을 때도 추가
                # 다시 상태 초기화
                prev = s[j:j+step]
                count = 1  # 수정: 초기화
                
        # 남아 있는 문자열에 대해서 처리
        if count >= 2:
            compressed += str(count) + prev
        else:
            compressed += prev
        
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    return answer
