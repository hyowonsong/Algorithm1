def solution(X, Y):
    # 각 숫자의 출현 횟수를 저장할 딕셔너리 생성
    x_count = {}
    y_count = {}
    for i in range(10):
        x_count[str(i)] = 0
        y_count[str(i)] = 0
    
    # X의 각 숫자 출현 횟수 계산
    for num in X:
        x_count[num] += 1
    
    # Y의 각 숫자 출현 횟수 계산
    for num in Y:
        y_count[num] += 1
    
    # 공통으로 나타나는 숫자들을 찾아 결과 리스트 생성
    result = []
    for i in range(9, -1, -1):  # 9부터 0까지 역순으로
        num = str(i)
        x_num_count = x_count[num]
        y_num_count = y_count[num]
        common_count = min(x_num_count, y_num_count)
        
        for _ in range(common_count):
            result.append(num)
    
    # 결과 처리
    if len(result) == 0:
        return "-1"
    
    if result[0] == "0":
        return "0"
    
    # 결과 리스트를 문자열로 변환
    return "".join(result)