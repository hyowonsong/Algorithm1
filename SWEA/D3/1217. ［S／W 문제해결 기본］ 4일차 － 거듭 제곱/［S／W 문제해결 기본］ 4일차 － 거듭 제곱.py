
T = 10

for t in range(1, T+1):
    n = int(input()) 
    a, b = map(int, input().split())  

     # 결과 초기값을 1로 설정, result 값 설정 중요!
    result = 1 


    while b > 0:
        result *= a  #
        b -= 1  

    print(f'#{n} {result}')  