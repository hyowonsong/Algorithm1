# 숫자 문자열과 영단어

def solution(s):
    dict = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    
    result = ""
    temp = ""
    
    for char in s:
        # char를 하나씩 돌면서 숫자면 한번에 걸리니까 result에 넣어준다.
        # 현재 문자가 숫자인 경우
        if char.isdigit():
            result += char
        # 현재 문자가 숫자가 아닌 경우
        else:
            temp += char
            if temp in dict:
                result += dict[temp]
                # temp 반드시 초기화 해줘야
                temp = ""
    
    return int(result)
