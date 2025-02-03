def bracket(s):
    stack = []
    for i in s:
        if len(stack) == 0: 
            stack.append(i)
        # 여기에 else문이 걸린다.
        else:
            if i == ")" and stack[-1] == "(":   
                stack.pop()
            elif i == "]" and stack[-1] == "[":   
                stack.pop()
            elif i == "}" and stack[-1] == "{":   
                stack.pop()
            else: 
                stack.append(i)

    if len(stack) == 0:
        return True
    else:
        return 0

        
def solution(s):
    answer = 0
    for i in range(len(s)):
        # 위의 bracket(s) 의 정의가 맞으면 answer +=1이다.
        if bracket(s):  
            answer +=1
        s = s[1:] + s[:1]  # 문자열 's'를 왼쪽으로 한 칸 회전하는 연산
    return answer