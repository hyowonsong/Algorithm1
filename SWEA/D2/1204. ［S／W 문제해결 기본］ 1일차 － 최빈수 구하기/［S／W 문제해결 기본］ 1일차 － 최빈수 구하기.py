# 최빈수 구하기
# 1000명의 수학 성적을 토대로 통계 자료

T = int(input())  

for i in range(1, T + 1):
    n = int(input())  
    numbers = list(map(int, input().split()))  
    frequency_dict = {}  

    # 점수 빈도수 계산
    for number in numbers:
        if number in frequency_dict:
            frequency_dict[number] += 1
        else:
            frequency_dict[number] = 1

    # 최빈수 및 최빈수의 최대값 초기화
    max_frequency = 0
    mode_value = 0

    # 딕셔너리를 통해 최빈수를 찾음
    for number, frequency in frequency_dict.items():
        # 현재 수가 더 높은 빈도수를 가지거나, 같은 빈도에서 수가 더 큰 경우
        if frequency > max_frequency or (frequency == max_frequency and number > mode_value):
            max_frequency = frequency  # 빈도수 업데이트
            mode_value = number  # 최빈수 업데이트

    # 결과 출력
    print(f'#{i} {mode_value}')  # 테스트 케이스 번호와 최빈수 출력
