# 17413 단어 뒤집기2
# 단어만 뒤집으려고 한다.
# 괄호 안에 있는 건 안 뒤집는다.

s = input()
temp = []
answer = []

for i in range(len(s)):
    # 닫힌 괄호가 있으면 그대로 추가
    if s[i] == '>':
        temp.append('>')
        answer.append(''.join(temp))
        # 임시 리스트 초기화
        temp = []
    # 열린 괄호가 나왔는데 이전 입력된 것들이 있따면    
    elif s[i] == '<' and temp:
        # 임시 리스트를 뒤집어서 초기화
        temp.reverse()
        answer.append(''.join(temp))
        # 임시 리스트 초기화
        temp = [s[i]]
    
    # 공백문자인데 괄호밖이라면
    elif s[i] == ' ' and '<' not in temp:
        temp.reverse()
        answer.append(''.join(temp))
        answer.append(' ')
        # 임시 변수 초기화
        temp = []
        
    else:
        temp.append(s[i])
        
# 아직 임시변수에 문자열 남아 있따면 추가
if temp:
    temp.reverse()
    answer.append(''.join(temp))
print(''.join(answer))