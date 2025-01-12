# 보석 쇼핑

def solution(gems):
    n = len(gems)
    gem_types = len(set(gems))  # 보석의 총 종류 수
    
    if gem_types == 1:  # 보석이 한 종류밖에 없다면
        return [1, 1]
    
    # 각 보석의 개수를 저장할 딕셔너리
    dict = {}
    answer = [1, n]  # 초기값은 전체 구간
    
    # two pointers
    start = 0
    end = 0
    
    # 투포인터를 할 때는 while문으로 end가 n보다 작을때까지
    while end < n:
        # end 포인터 진행
        dict[gems[end]] = dict.get(gems[end], 0) + 1
        end += 1
        
        # 현재 구간에 모든 종류의 보석이 있다면
        while len(dict) == gem_types:
            # 더 짧은 구간을 발견하면 정답 갱신
            if end - start < answer[1] - answer[0] + 1:
                answer = [start + 1, end]
            
            # start 포인터 진행
            dict[gems[start]] -= 1
            if dict[gems[start]] == 0:
                del dict[gems[start]]
            start += 1
    
    return answer