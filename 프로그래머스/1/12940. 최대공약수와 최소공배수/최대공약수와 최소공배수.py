# 최대공약수와 최소공배수
def solution(n,m):
    answer =[]
    # 최소 공약수를 저장할 리스트
    arr1=[]                 

    # 최소 공약수 구하기
    for i in range(1, min(n, m)+1):
        if n%i == 0 and m%i ==0: 
            arr1.append(i)

    # 최대 공약수 구하기
    for i in range(max(n, m), (n*m)+1):       
        # n,m 중 큰 값부터 n*m 곱한값 +1 까지 계속 for 문
        # 여기는 반대로 i가 n으로 나누어질 때 min_num = i 이다.
        # 최대공약수는 두 수의 공통된 약수 중에서 가장 큰 수를 찾는 것
        if i%n == 0 and i%m == 0:              
            min_num = i                       
            break

    max_num = max(arr1)
    answer = [max_num, min_num]
    return answer
