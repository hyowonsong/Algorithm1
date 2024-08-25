def solution(files):
    # 파일명을 HEAD와 NUMBER로 파싱하는 함수
    def parse_file(file):
        head = ''   # HEAD 부분을 저장할 변수
        number = '' # NUMBER 부분을 저장할 변수
        i = 0
        length = len(file)
        
        # HEAD 추출: 숫자가 나오기 전까지 문자를 계속 추가
        while i < length and not file[i].isdigit():
            head += file[i]
            i += 1
        
        # NUMBER 추출: 숫자가 나오는 부분부터 최대 5자리까지 추출
        while i < length and file[i].isdigit():
            number += file[i]
            i += 1
        
        # TAIL은 정렬에 필요 없으므로 추출하지 않음
        return (head, number)
    
    # 정렬을 위한 키 함수
    def sort_key(file):
        head, number = parse_file(file)
        return (head.lower(), int(number))
    
    # 파일명 리스트를 정렬 기준에 맞게 정렬하여 반환
    return sorted(files, key=sort_key)