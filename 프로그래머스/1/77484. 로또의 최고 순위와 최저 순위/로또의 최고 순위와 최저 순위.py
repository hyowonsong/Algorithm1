def solution(lottos, win_nums):
    success = 0
    random = 0

    # 맞힌 번호와 0의 개수를 계산합니다.
    for num in lottos:
        if num in win_nums:
            success += 1
        elif num == 0:
            random += 1

    # 맞힌 개수에 따라 순위를 계산하는 함수
    def get_rank(matches):
        if matches >= 6:
            return 1
        elif matches == 5:
            return 2
        elif matches == 4:
            return 3
        elif matches == 3:
            return 4
        elif matches == 2:
            return 5
        else:
            return 6

    # 최고 순위와 최저 순위 계산
    max_rank = get_rank(success + random)
    min_rank = get_rank(success)

    return [max_rank, min_rank]