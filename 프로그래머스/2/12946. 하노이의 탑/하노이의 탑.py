
def move(n, from_pole, to_pole, second_pole, answer):
    if n == 1:
        # 원판 하나를 옮기는 경우
        answer.append([from_pole, to_pole])
        return
    
    # n-1개의 원판을 보조 기둥으로 옮깁니다.
    move(n-1, from_pole, second_pole, to_pole, answer)
    # 가장 큰 원판을 목표 기둥으로 옮깁니다.
    answer.append([from_pole, to_pole])
    # 보조 기둥에 있는 n-1개의 원판을 목표 기둥으로 옮깁니다.
    move(n-1, second_pole, to_pole, from_pole, answer)

def solution(n):
    answer = []
    move(n, 1, 3, 2, answer)  # 1번 기둥에서 3번 기둥으로 n개의 원판을 옮깁니다.
    return answer