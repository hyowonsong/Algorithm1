# 자릿수 더하기
# 그냥 int(input()) 말고 input() 으로 받으면 자릿수끼리 더하기 가능

N = input() 
total = 0

# 문자열 N의 각 문자를 순회이기 때문에 range 사용하면 안된다
for i in N:
    total += int(i)  
    
print(total)  


