def dfs(order, course_len, current_idx, current_course, result):
    if len(current_course) == course_len:
        result.append(''.join(sorted(current_course)))
        return
    
    for i in range(current_idx, len(order)):
        current_course.append(order[i])
        dfs(order, course_len, i + 1, current_course, result)
        current_course.pop()

def solution(orders, course):
    answer = []
    
    # 각 코스 길이별로 처리
    for course_len in course:
        # 각 주문별로 가능한 모든 조합 찾기
        combinations = []
        for order in orders:
            result = []
            dfs(order, course_len, 0, [], result)
            combinations.extend(result)
        
        # 각 조합이 몇 번 등장했는지 카운트
        count_dict = {}
        for comb in combinations:
            count = 0
            for order in orders:
                # 현재 조합이 주문에 모두 포함되어 있는지 확인
                is_contained = True
                for c in comb:
                    if c not in order:
                        is_contained = False
                        break
                if is_contained:
                    count += 1
            if count >= 2:  # 2명 이상이 주문한 경우만 저장
                count_dict[comb] = count
        
        # 가장 많이 주문된 조합 찾기
        if count_dict:
            max_count = max(count_dict.values())
            for comb, count in count_dict.items():
                if count == max_count:
                    answer.append(comb)
    
    return sorted(answer)