
def solution(X, Y):
    answer = []
    
    # 0부터 9까지의 숫자에 대해
    for i in range(9, -1, -1):  # 9부터 0까지 역순으로
        digit = str(i)
        # X와 Y에서 해당 숫자의 개수를 세고, 그 중 작은 값을 선택
        count = min(X.count(digit), Y.count(digit))
        # 선택된 개수만큼 결과 리스트에 추가
        answer.extend([digit] * count)
    
    # 결과 처리
    if not answer:
        return "-1"
    if answer[0] == "0":
        return "0"
    
    return "".join(answer)