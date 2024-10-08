# 과목 평점에 대한 매핑
grade_points = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0,
    'P': None  # P는 계산에서 제외
}

total_credits = 0  # 총 학점
weighted_sum = 0.0  # (학점 × 과목평점)의 합

# 20줄의 입력 처리
for _ in range(20):
    line = input()
    subject, credits, grade = line.split()  # 과목명, 학점, 등급
    credits = float(credits)  # 학점을 float로 변환
    point = grade_points[grade]  # 해당 등급의 평점을 가져옴

    if point is not None:  # P등급이 아닐 경우
        total_credits += credits  # 총 학점을 업데이트
        weighted_sum += credits * point 

# 전공평점 계산
if total_credits > 0:  # 총 학점이 0보다 크면
    major_gpa = weighted_sum / total_credits
else:
    major_gpa = 0.0  # 총 학점이 0이면 GPA는 0으로 설정

# 소수점 6자리까지
print(f"{major_gpa:.6f}") 