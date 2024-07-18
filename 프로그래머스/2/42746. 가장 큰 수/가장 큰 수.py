def solution(numbers):
    # 숫자를 문자열로 변환
    str_numbers = list(map(str, numbers))
    
    # 비교 함수 정의
    def compare(x, y):
        # x가 y 보다 앞에 오는 것들
        if x + y > y + x:
            return -1
        # y가 x보다 앞에 오는 것들
        elif x + y < y + x:
            return 1
        # x와 y 순서 상관 없는 경우
        else:
            return 0
    
    # 퀵 정렬
    # pivot을 정하고 left(왼쪽), right(오른쪽) 를 정하고 
    # left는 pivot보다 큰 경우 right는 pivot 보다 작은 경우로 서로 바꾸기
    def quicksort(arr):
        # arr의 길이가 1 이하이면 이미 정렬된 상태이므로 그대로 반환
        if len(arr) <= 1:
            return arr
        # pivot을 리스트의 중앙값으로 설정
        pivot = arr[len(arr) // 2]
        
        # left는 pivot 보다 앞에 와야 하는 요소들로 구성
        left = []
        for x in arr:
            if compare(x, pivot) == -1:
                left.append(x)

        # middle은 pivot과 동일한 요소들로 구성
        middle = []
        for x in arr:
            if compare(x, pivot) == 0:
                middle.append(x)

        # right는 pivot보다 뒤에 와야하는 요소들로 구성
        right = []
        for x in arr:
            if compare(x, pivot) == 1:
                right.append(x)
        # quicksort 함수를 재귀적으로 호출
        return quicksort(left) + middle + quicksort(right)
    
    sorted_numbers = quicksort(str_numbers)
    
    # 정렬된 숫자들을 이어 붙임
    largest_number = ''.join(sorted_numbers)
    
    # 모든 숫자가 0인 경우 "000..."이 되므로 이때는 "0"을 반환
    if largest_number[0] == '0':
        return '0'
    # 그렇지 않은 경우 largest_number를 그대로 반환
    else:
        return largest_number