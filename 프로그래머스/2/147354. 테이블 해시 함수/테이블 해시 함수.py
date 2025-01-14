def solution(data, col, row_begin, row_end):
    # 1. 데이터 정렬
    data.sort(key=lambda x: (x[col - 1], -x[0]))  # col 기준 오름차순, 기본키 기준 내림차순
    
    # 2. S_i 계산 및 XOR 누적
    result = 0  
    
    # row_begin부터 row_end까지 각 행을 순차적으로 반복
    for i in range(row_begin, row_end + 1):
        # i번째 행에서 각 컬럼 값에 대해 나머지를 구하고 그 값을 모두 더함
        S_i = 0
        for value in data[i - 1]:  # data[i - 1]은 i번째 행을 의미
            S_i += value % i  
        
        # 계산된 S_i 값을 result와 XOR 연산하여 누적
        result ^= S_i  
    
    return result  