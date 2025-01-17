# DFS로 할인율 조합 생성
def dfs(depth, current, result, discount_rates, m):
    if depth == m:  # 모든 이모티콘에 대해 할인율을 설정했으면 결과에 추가
        result.append(current[:])
        return
    for rate in discount_rates:
        current.append(rate)
        dfs(depth + 1, current, result, discount_rates, m)
        current.pop()  # 백트래킹

# 메인 solution 함수
def solution(users, emoticons):
    discount_rates = [10, 20, 30, 40]
    m = len(emoticons)
    all_discount = []

    # DFS로 할인율 조합 생성
    dfs(0, [], all_discount, discount_rates, m)

    max_plus_users = 0  # 최대 플러스 서비스 가입자 수
    max_sales = 0       # 최대 매출액

    # 각 할인율 조합에 대해 결과 계산
    for discounts in all_discount:
        plus_users = 0
        sales = 0

        for user_rate, user_price in users:  # 각 사용자 처리
            total_cost = 0

            # 사용자가 구매 가능한 이모티콘 계산
            for i in range(m):
                if discounts[i] >= user_rate:  # 할인율 조건 만족
                    discounted_price = emoticons[i] * (100 - discounts[i]) // 100
                    total_cost += discounted_price

            # 기준에 따라 플러스 서비스 가입 또는 매출 합산
            if total_cost >= user_price:
                plus_users += 1
            else:
                sales += total_cost

        # 목표 1: 플러스 서비스 가입자 수 최대화, 목표 2: 매출액 최대화
        if plus_users > max_plus_users or (plus_users == max_plus_users and sales > max_sales):
            max_plus_users = plus_users
            max_sales = sales

    return [max_plus_users, max_sales]