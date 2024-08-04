# 최대공약수와 최소공배수
def solution(n,m):
    answer =[]
    arr1=[]                 # 공약수를 저장할 리스트

    for i in range(1, min(n, m)+1):
        if n%i == 0 and m%i ==0: # 동시에 나눠지면 공약수
            arr1.append(i)

    for i in range(max(n, m), (n*m)+1):       
        # n,m 중 큰 값부터 n*m 곱한값 +1 까지 계속 for 문
        if i%n == 0 and i%m == 0:             # 둘다 0으로 나누어진다면 
            min_num = i                       # min_num = i 
            break

    max_num = max(arr1)
    answer = [max_num, min_num]
    return answer
