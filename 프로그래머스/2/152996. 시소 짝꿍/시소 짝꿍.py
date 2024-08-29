from collections import Counter

def solution(weights):
    count = 0
    weight_count = Counter(weights)
    
    # 같은 무게로 쌍을 이룰 때
    for weight in weight_count:
        if weight_count[weight] > 1:
            count += (weight_count[weight] * (weight_count[weight] - 1)) // 2
    
    # 다른 무게로 쌍을 이룰 때
    # 가능한 비율: (2/3, 3/2), (2/4, 4/2), (3/4, 4/3)
    for weight in weight_count:
        if weight * 2 in weight_count:
            count += weight_count[weight] * weight_count[weight * 2]
        if weight * 3 % 2 == 0 and weight * 3 // 2 in weight_count:
            count += weight_count[weight] * weight_count[weight * 3 // 2]
        if weight * 4 % 3 == 0 and weight * 4 // 3 in weight_count:
            count += weight_count[weight] * weight_count[weight * 4 // 3]
    
    return count
