N = input()  
# 0~9 숫자의 개수를 저장할 리스트
count = [0] * 10  

# 각 숫자의 개수 세기
for digit in N:
    count[int(digit)] += 1

# 6과 9는 서로 바꿔서 사용할 수 있으므로 합쳐서 처리
# 합친 개수를 2로 나누고 올림하여 필요한 세트 개수 계산
total_69 = count[6] + count[9]
count[6] = (total_69 + 1) // 2
count[9] = count[6]  # 6과 9는 같은 세트 개수가 필요

# 가장 많이 필요한 숫자의 개수가 필요한 세트의 개수
result = max(count)
print(result)