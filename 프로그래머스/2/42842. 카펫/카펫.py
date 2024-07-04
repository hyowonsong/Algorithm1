def solution(brown, yellow):
    total_area = brown + yellow

    for height in range(1, int(total_area**0.5) + 1):
        if total_area % height == 0:
            width = total_area // height
            if width >= height:
                # 가장자리 갈색 격자의 수 확인
                if (width + height - 2) * 2 == brown:
                    return [width, height]