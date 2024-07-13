from collections import defaultdict
import math

def calculate_fee(time, fees):
    basic_time, basic_fee, unit_time, unit_fee = fees
    if time <= basic_time:
        return basic_fee
    else:
        return basic_fee + math.ceil((time - basic_time) / unit_time) * unit_fee

def solution(fees, records):
    in_time = {}
    total_time = defaultdict(int)

    for record in records:
        time, car_number, status = record.split()
        hh, mm = map(int, time.split(':'))
        minutes = hh * 60 + mm
        
        if status == "IN":
            in_time[car_number] = minutes
        elif status == "OUT":
            total_time[car_number] += minutes - in_time[car_number]
            del in_time[car_number]

    # 출차 기록이 없는 차량은 23:59에 출차한 것으로 간주
    for car_number, minutes in in_time.items():
        total_time[car_number] += 23 * 60 + 59 - minutes

    # 차량 번호가 작은 자동차부터 청구할 주차 요금을 계산
    result = []
    for car_number in sorted(total_time):
        fee = calculate_fee(total_time[car_number], fees)
        result.append(fee)

    return result

# 테스트 케이스
fees = [180, 5000, 10, 600]
records = [
    "05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", 
    "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"
]
print(solution(fees, records))  # 예상 결과: [14600, 34400, 5000]
