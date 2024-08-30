from collections import Counter

def solution(weights):
    count = Counter(weights)
    pairs = 0
    
    for weight in count:
        freq = count[weight]
        # 같은 무게의 경우
        pairs += freq * (freq - 1) // 2
        
        # 2:3 비율 체크
        if weight * 2 % 3 == 0:
            partner_weight = weight * 2 // 3
            if partner_weight in count:
                pairs += freq * count[partner_weight]
        
        # 2:4 (1:2) 비율 체크
        partner_weight = weight * 2
        if partner_weight in count:
            pairs += freq * count[partner_weight]
        
        # 3:4 비율 체크
        if weight * 3 % 4 == 0:
            partner_weight = weight * 3 // 4
            if partner_weight in count:
                pairs += freq * count[partner_weight]
    
    return pairs