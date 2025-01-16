def solution(enroll, referral, seller, amount):
    # 1. 추천인 관계 및 초기 수익 세팅
    parent = {}
    profit = {}
    
    for i in range(len(enroll)):
        parent[enroll[i]] = referral[i]
        profit[enroll[i]] = 0
    profit["center"] = 0  # 센터(민호) 추가

    # 2. 이익 분배
    for i in range(len(seller)):
        current = seller[i]
        income = amount[i] * 100  # 칫솔 1개당 100원 수익

        while current != "-":
            commission = income // 10  # 10% 수익
            profit[current] += income - commission  # 본인 수익

            # 분배 금액이 1원 미만이면 종료
            if commission == 0:
                break

            # 추천인에게 분배
            current = parent.get(current, "center")
            income = commission

    # 3. 결과 반환
    result = []
    for name in enroll:
        result.append(profit[name])
    
    return result