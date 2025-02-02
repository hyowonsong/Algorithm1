def solution(want, number, discount):
    want_dict = {}
    for i in range(len(want)):
        want_dict[want[i]] = number[i]

    total_days = 0

    # 10일 동안의 할인 목록 검사
    for start in range(len(discount) - 9):
        # 현재 10일간의 할인 목록 추출
        current_discount = discount[start:start + 10]
        current_count = {}

        # 현재 10일 동안의 제품과 수량 세기
        for item in current_discount:
            if item in current_count:
                current_count[item] += 1
            else:
                current_count[item] = 1

        # 원하는 제품 수량과 일치하는지 확인
        valid = True
        # 하나하나 for문을 돌아다니면서 같은지 체크 
        for item in want_dict:
            # 현재 카운트에 해당 제품이 없다면 valid=False
            if item not in current_count or current_count[item] != want_dict[item]:
                valid = False
                break

        # 유효하다면 총 일수 증가
        if valid:
            total_days += 1

    return total_days