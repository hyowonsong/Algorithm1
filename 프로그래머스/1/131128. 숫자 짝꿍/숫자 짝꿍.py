# 숫자 짝궁
# 두 정수 X,Y 의 임의의 자리에서 공통으로 만들 수 있는 가장 큰 정수는?

def solution(X, Y):
    answer = []
    
    # 9부터 0까지 역순으로 각 숫자 확인
    for i in range(9,-1,-1):
        
        # X와 Y에서 현재 숫자(digit)의 출현 횟수를 세고, 그 중 작은 값을 선택
        count = min(X.count(str(i)), Y.count(str(i)))
        
        # 선택된 개수(count)만큼 현재 숫자(digit)를 결과 리스트에 추가
        answer.extend([str(i)] * count)

    if not answer:
        return "-1"
        # answer의 첫 숫자가 0이면 모든 공통된 숫자가 0이라는 뜻이므로 "0" 반환
    if answer[0]  == "0":
        return "0"
    
    # answer 리스트의 모든 숫자를 하나의 문자열로 연결하여 반환
    return "".join(answer)
