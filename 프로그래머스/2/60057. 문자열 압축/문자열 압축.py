def solution(s):
    answer = len(s)  # 초기 답은 문자열의 길이로 설정

    # 1부터 문자열 길이의 절반까지를 압축 단위로 설정하여 검사
    for i in range(1, len(s) // 2 + 1):
        pos = 0  # 현재 압축을 시작할 위치
        length = len(s)  # 압축 후 문자열의 길이를 추적

        # 현재 압축 단위로 문자열을 확인
        while pos + i <= len(s):
            unit = s[pos:pos + i]  # 압축 단위만큼의 문자열 추출
            pos += i  # 압축 단위만큼 위치를 이동

            cnt = 0  # 반복되는 부분 문자열의 개수

            # 반복되는 부분 문자열을 체크
            while pos + i <= len(s) and s[pos:pos + i] == unit:
                cnt += 1
                pos += i

            # 압축이 발생한 경우
            if cnt > 0:
                length -= i * cnt  # 중복된 문자열만큼 길이를 줄임
                # 압축된 횟수에 따라 추가되는 길이 계산
                if cnt < 9:
                    length += 1  # "2"처럼 1자리 숫자
                elif cnt < 99:
                    length += 2  # "10"처럼 2자리 숫자
                elif cnt < 999:
                    length += 3  # "100"처럼 3자리 숫자
                else:
                    length += 4  # "1000"처럼 4자리 숫자

        # 최소 길이를 갱신
        answer = min(answer, length)

    return answer
