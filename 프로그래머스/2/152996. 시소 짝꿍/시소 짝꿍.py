from collections import Counter

def solution(weights):
    answer = 0
    # 각 무게의 빈도수를 계산
    weight_counts = Counter(weights)
    
    # 중복을 피하기 위해 고유한 무게들에 대해 반복
    for weight in set(weights):
        # 같은 무게의 경우
        if weight_counts[weight] > 1:
            # nC2 조합 계산: n * (n-1) / 2
            answer += weight_counts[weight] * (weight_counts[weight] - 1) // 2
        
        # 다른 무게의 경우
        # 가능한 비율: 2m/3m, 3m/4m, 2m/4m
        for ratio in [2/3, 3/4, 2/4]:
            # 짝꿍의 무게 계산
            partner_weight = weight * ratio
            # 짝꿍의 무게가 존재하는 경우
            if partner_weight in weight_counts:
                # 현재 무게의 빈도수 * 짝꿍 무게의 빈도수
                answer += weight_counts[weight] * weight_counts[partner_weight]
    
    return answer