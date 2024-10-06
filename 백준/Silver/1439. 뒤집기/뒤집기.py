# 문자열 뒤집기

# 문자열 S에 있는 모든 숫자를 전부 같게 만들기
# 연속된 하나 이상의 숫자를 잡고 모두 뒤집기
# 다솜이가 해야 하는 행동의 최소 횟수 출력

String = input()
count0 = 0
count1 = 0


if String[0] == '1':
    count0 += 1
else:
    count1 += 1

# 맨처음 숫자에서 다른 숫자로 바뀌는 순간 += 1
for i in range(len(String)-1):
    if String[i] != String[i+1]:
            # 다음 수에서 1로 바뀌는 경우 0으로 다 바꿔줘야하니까 count0 +=1이다.
        if String[i+1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))


