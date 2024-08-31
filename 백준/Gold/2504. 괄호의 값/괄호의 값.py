# 괄호의 값

arr = input() 
stack = [] 
answer = 0  
tmp = 1  

for i in range(len(arr)):
    if arr[i] == '(':
        stack.append(arr[i])  # 열린 괄호를 스택에 추가
        tmp *= 2  # 괄호의 값에 2를 곱함
    elif arr[i] == '[':
        stack.append(arr[i])  # 열린 대괄호를 스택에 추가
        tmp *= 3  # 괄호의 값에 3을 곱함

    elif arr[i] == ')':
        if not stack or stack[-1] == "[":
            answer = 0  # 잘못된 괄호열: 미스매치 발생
            break
        if arr[i-1] == "(":
            answer += tmp  # 올바른 괄호 쌍: 괄호값을 추가
        stack.pop()  # 열린 괄호를 스택에서 제거
        tmp //= 2  # 현재 괄호의 값을 2로 나눔

    elif arr[i] == ']':
        if not stack or stack[-1] == "(":
            answer = 0  # 잘못된 괄호열: 미스매치 발생
            break
        
        if arr[i-1] == '[':
            answer += tmp  # 올바른 괄호 쌍: 괄호값을 추가
        stack.pop()  # 열린 대괄호를 스택에서 제거
        tmp //= 3  # 현재 괄호의 값을 3으로 나눔

if stack:
    print(0)  # 스택에 괄호가 남아있으면 유효하지 않음
else:
    print(answer)  # 올바른 괄호열의 총 값을 출력