def solution(files):
    def split_filename(filename):
        head = ""
        number = ""
        tail = ""
        
        # HEAD 부분 찾기
        for i, char in enumerate(filename):
            if char.isdigit():
                break
            head += char
        
        # NUMBER 부분 찾기
        for char in filename[i:]:
            if not char.isdigit():
                break
            if len(number) >= 5:
                break
            number += char
        
        # TAIL은 나머지 부분
        tail = filename[i + len(number):]
        
        return head, number, tail

    def compare(file_info):
        head, number, _, index = file_info
        return (head.lower(), int(number), index)

    # 파일명을 분리하고 원래 인덱스와 함께 저장
    file_infos = [(split_filename(f) + (i,)) for i, f in enumerate(files)]
    
    # 정렬
    sorted_files = sorted(file_infos, key=compare)
    
    # 정렬된 순서대로 원래 파일명 반환
    return [files[info[3]] for info in sorted_files]