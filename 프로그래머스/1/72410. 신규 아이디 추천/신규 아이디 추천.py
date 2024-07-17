import re  # 정규표현식을 사용하기 위한 모듈 import

def solution(new_id):
    # 1단계: 모든 대문자를 소문자로 변환
    new_id = new_id.lower()
    
    # 2단계: 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자 제거
    # re.sub(pattern, repl, string): string에서 pattern과 일치하는 부분을 repl로 치환
    # r'[^a-z0-9\-_.]': ^ 는 not을 의미. 즉, 소문자, 숫자, -, _, . 을 제외한 모든 문자를 의미
    new_id = re.sub(r'[^a-z0-9\-_.]', '', new_id)
    
    # 3단계: 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    # '\.+': \. 는 문자 '.'를 의미하고, + 는 1회 이상 반복을 의미
    # 따라서 '.'이 1회 이상 반복되는 부분을 찾아 '.' 하나로 치환
    new_id = re.sub('\.+', '.', new_id)
    
    # 4단계: 마침표(.)가 처음이나 끝에 위치한다면 제거
    new_id = new_id.strip('.')
    
    # 5단계: 빈 문자열이라면, "a"를 대입
    if not new_id:
        new_id = 'a'
    
    # 6단계: 길이가 16자 이상이면, 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    # 만약 제거 후 마침표(.)가 끝에 위치한다면 마침표(.) 문자를 제거
    if len(new_id) >= 16:
        new_id = new_id[:15].rstrip('.')
    
    # 7단계: 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 붙임
    while len(new_id) <= 2:
        new_id += new_id[-1]
    
    return new_id