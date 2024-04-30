# 실패율

def solution(N, stages):
    results = {}
    length = len(stages)

    # 1부터 N까지 스테이지를 하나씩 살펴봄
    for n in range(1, N+1):
        if length != 0:  # 만약 남은 플레이어가 있다면
            count = stages.count(n)  # 해당 스테이지를 클리어하지 못한 플레이어의 수를 센다
            results[n] = count / length  # 실패율 계산 (클리어하지 못한 플레이어 수 / 현재 스테이지에 도달한 플레이어 수)
            length -= count  # 남은 플레이어 수 업데이트
        else:
            results[n] = 0  # 만약 도달한 플레이어가 없다면 실패율은 0

    # 실패율이 높은 순서로 스테이지를 정렬하여 반환
    return sorted(results, key=lambda x: results[x], reverse=True)
