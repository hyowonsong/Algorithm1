def gcd(a, b):
    while b != 0: 
        a, b = b, a % b  
    return a 

def solution(w, h):
    # 사용할 수 있는 정사각형의 개수를 반환하는 함수
    return w * h - (w + h - gcd(w, h))  # 전체 사각형 - 대각선이 지나는 사각형
