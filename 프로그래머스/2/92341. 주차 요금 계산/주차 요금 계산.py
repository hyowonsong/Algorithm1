# 주차 요금 계산

# 주차장의 요금표(fess), 기록(records)이 주어짐.
# 차량별로 주차 요금을 계산하자.

# fees는 기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)
# records에는 (입,출)차시간, 차량 번호, 내역이 있습니다.

def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    parking_records = {}  # 차량별 입차 시간 저장
    total_time = {}  # 차량별 누적 주차 시간 저장

    def calculate_time(in_time, out_time):
        in_h, in_m = map(int, in_time.split(":"))
        out_h, out_m = map(int, out_time.split(":"))
        return (out_h * 60 + out_m) - (in_h * 60 + in_m)

    for record in records:
        time, car_number, status = record.split()
        
        if status == "IN":
            parking_records[car_number] = time
        else:  # "OUT"인 경우
            parked_time = calculate_time(parking_records[car_number], time)
            if car_number in total_time:
                total_time[car_number] += parked_time
            else:
                total_time[car_number] = parked_time
            del parking_records[car_number]  # 출차 완료된 차량 삭제

    # 23:59까지 출차되지 않은 차량 처리
    for car_number in parking_records:
        parked_time = calculate_time(parking_records[car_number], "23:59")
        if car_number in total_time:
            total_time[car_number] += parked_time
        else:
            total_time[car_number] = parked_time

    # 요금 계산 함수
    def calculate_fee(parked_time):
        if parked_time <= base_time:
            return base_fee
        extra_time = parked_time - base_time
        extra_fee = ((extra_time + unit_time - 1) // unit_time) * unit_fee  # 올림 처리
        return base_fee + extra_fee

    # 차량 번호 기준 정렬 후 요금 계산
    sorted_cars = sorted(total_time.keys())
    result = []
    for car_number in sorted_cars:
        result.append(calculate_fee(total_time[car_number]))
    
    return result