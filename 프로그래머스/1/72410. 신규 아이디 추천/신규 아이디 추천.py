def solution(new_id):
    # 1단계: 모든 대문자를 소문자로 치환
    new_id = new_id.lower()

    # 2단계: 허용된 문자 외의 모든 문자를 제거
    allowed_chars = set('abcdefghijklmnopqrstuvwxyz0123456789-_.')
    new_id = ''.join(char for char in new_id if char in allowed_chars)

    # 3단계: 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    # 4단계: 마침표(.)가 처음이나 끝에 위치한다면 제거
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]

    # 5단계: new_id가 빈 문자열이라면, "a"를 대입
    if not new_id:
        new_id = 'a'

    # 6단계: new_id의 길이가 16자 이상이면, 첫 15자의 문자 제외한 나머지 제거
    if len(new_id) > 15:
        new_id = new_id[:15]
        # 제거 후 마침표가 끝에 위치하면 제거
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # 7단계: new_id의 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복해서 붙임
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id