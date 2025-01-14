# 개인정보 수집 유효기간

# 고객의 약관 동의를 얻어서 수집된 1~n번으로 분류되는 개인정보 n개 있다.
# 각 약관마다 개인정보 보관 유효기간이 정해져 있음
# 오늘 날짜로 파기해야 할 개인정보 번호들을 구해보자(모든 달은 28일까지!)

# [입력] : 오늘 날짜를 의미하는 문자열 today, 약관의 유효기간을 담은 terms
# 수집된 개인정보의 정보를 담은 1차원 문자열 배열 privacies가 매개변수
# 이때, 파기해야 할 개인정보의 번호를 오름차순으로 1차원 정수 배열에 담아 return

def solution(today, terms, privacies):
    # 날짜를 총 일수로 변환하는 함수
    def date_to_days(year, month, day):
        return (year * 12 * 28) + (month * 28) + day

    # 오늘 날짜 처리
    today_year, today_month, today_day = map(int, today.split('.'))
    today_days = date_to_days(today_year, today_month, today_day)

    # 약관 정보를 딕셔너리로 변환
    term_dict = {}
    for term in terms:
        term_type, duration = term.split()
        term_dict[term_type] = int(duration) * 28  # 월을 일 단위로 변환

    # 결과 저장 리스트
    result = []

    # 개인정보 처리
    for idx, privacy in enumerate(privacies):
        privacy_date, term_type = privacy.split()
        privacy_year, privacy_month, privacy_day = map(int, privacy_date.split('.'))
        
        # 수집 일자를 일 단위로 변환 후 약관의 유효기간을 더함
        privacy_days = date_to_days(privacy_year, privacy_month, privacy_day)
        expiry_days = privacy_days + term_dict[term_type]
        
        # 유효기간 만료 날짜를 today와 비교
        if expiry_days <= today_days:
            result.append(idx + 1)

    return result