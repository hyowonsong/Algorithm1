# 회원등록시 원하는 제품을 모두 할인 받을 수 있는 회원등록 날짜 총 일수

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
        for item in want_dict:
            if current_count.get(item, 0) != want_dict[item]:
                valid = False
                break

        # 유효하다면 총 일수 증가
        if valid:
            total_days += 1

    return total_days
