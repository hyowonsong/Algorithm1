def solution(files):
    # 파일명을 HEAD와 NUMBER로 파싱하는 함수
    def parse_file(file):
        head = ""
        number = ""
        i = 0
        length = len(file)
        
        # HEAD 추출: 첫 번째 숫자가 나올 때까지 문자 추가
        while i < length and not file[i].isdigit():
            head += file[i]
            i += 1
        
        # NUMBER 추출: 숫자가 나오는 부분부터 최대 5자리까지
        while i < length and file[i].isdigit():
            number += file[i]
            i += 1
        
        return head, number
    
    # 정렬 기준 함수
    def sort_key(file):
        head, number = parse_file(file)
        return (head.lower(), int(number))  # HEAD: 소문자로 비교, NUMBER: 정수 비교
    
    # 파일명을 정렬 기준에 따라 정렬
    return sorted(files, key=sort_key)
