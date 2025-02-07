def solution(files):
    # 파일명을 HEAD와 NUMBER로 파싱하는 함수
    def parse_file(file):
        head = ""
        number = ""
        
        # HEAD 추출: 숫자가 나오기 전까지 문자 저장
        for i in range(len(file)):
            if file[i].isdigit():  # 숫자가 나오면 HEAD 추출 완료
                break
            head += file[i]
        
        # NUMBER 추출: 숫자가 나오면 최대 5자리까지 저장
        for j in range(i, len(file)):
            if not file[j].isdigit():  # 숫자가 끝나면 중단
                break
            if len(number) < 5:
                number += file[j]
        
        return head, number

    # 정렬 기준 함수
    def sort_key(file):
        head, number = parse_file(file)
        return (head.lower(), int(number))  # HEAD: 소문자로 비교, NUMBER: 정수 비교

    # 파일명을 정렬 기준에 따라 정렬
    return sorted(files, key=sort_key)