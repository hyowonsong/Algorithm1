# 기지국 설치

def solution(n, stations, w):
    answer = 0
    position = 1
    index = 0

    while position <= n:
        if index < len(stations) and position >= stations[index] - w:
            position = stations[index] + w + 1
            index += 1
        else:
            answer += 1
            position += 2 * w + 1

    return answer