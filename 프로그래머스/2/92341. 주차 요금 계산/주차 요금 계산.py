from collections import defaultdict
import math

# 주차 요금을 계산하는 함수
def calculate_fee(time, fees):
    # 요금표에서 기본 시간, 기본 요금, 단위 시간, 단위 요금을 가져옴
    basic_time, basic_fee, unit_time, unit_fee = fees

    # 누적 주차 시간이 기본 시간 이하면 기본 요금만 부과
    if time <= basic_time:
        return basic_fee
    else:
        # 기본 시간을 초과한 경우, 초과 시간에 대해 단위 요금을 계산하여 부과
        return basic_fee + math.ceil((time - basic_time) / unit_time) * unit_fee

# 주차 요금을 계산하는 메인 함수
def solution(fees, records):
    # 입차 시간을 저장할 딕셔너리
    in_time = {}

    # 차량별 누적 주차 시간을 저장할 딕셔너리 (초기값 0)
    total_time = defaultdict(int)

    # 입출차 기록을 순회하면서 주차 시간을 계산
    for record in records:
        # 각 기록을 시간, 차량 번호, 상태로 분리
        time, car_number, status = record.split()
        
        # 시각을 분 단위로 변환
        hh, mm = map(int, time.split(':'))
        minutes = hh * 60 + mm
        
        if status == "IN":
            # 입차한 경우, in_time 딕셔너리에 입차 시간을 저장
            in_time[car_number] = minutes
        elif status == "OUT":
            # 출차한 경우, 해당 차량의 주차 시간을 계산하여 total_time에 누적
            total_time[car_number] += minutes - in_time[car_number]
            # 출차 후에는 입차 기록을 삭제
            del in_time[car_number]

    # 출차 기록이 없는 차량은 23:59에 출차한 것으로 간주하고 시간 계산
    for car_number, minutes in in_time.items():
        total_time[car_number] += 23 * 60 + 59 - minutes

    # 차량 번호가 작은 순서대로 주차 요금을 계산
    result = []
    for car_number in sorted(total_time):
        # 누적 주차 시간을 바탕으로 요금을 계산
        fee = calculate_fee(total_time[car_number], fees)
        # 계산된 요금을 결과 리스트에 추가
        result.append(fee)

    return result