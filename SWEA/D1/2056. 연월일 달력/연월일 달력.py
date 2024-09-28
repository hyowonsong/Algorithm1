# 월을 나타내는 리스트 (01부터 12까지)
month_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

# 각 월에 해당하는 최대 일수를 나타내는 리스트
day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

# 테스트 케이스의 개수 입력
T = int(input())

# 각 테스트 케이스 처리
for test_case in range(1, T + 1):
    date = input()  # 8자리 날짜 입력 (YYYYMMDD)
    
    # 연, 월, 일 추출
    year = date[0:4]  # 연도
    month = date[4:6]  # 월
    day = date[6:8]  # 일
    
    # 월 유효성 검사
    if month in month_list:
        idx = int(month) - 1  # 월에 해당하는 인덱스
        # 일 유효성 검사
        if int(day) >= 1 and int(day) <= day_list[idx]:
            # 날짜가 유효하면 지정된 형식으로 출력
            print(f"#{test_case} {year}/{month}/{day}")
        else:
            # 날짜가 유효하지 않으면 -1 출력
            print(f"#{test_case} -1")
    else:
        # 월이 유효하지 않으면 -1 출력
        print(f"#{test_case} -1")
