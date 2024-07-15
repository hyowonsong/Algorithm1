def solution(numbers):
    # 숫자를 문자열로 변환
    str_numbers = list(map(str, numbers))
    
    # 비교 함수 정의
    def compare(x, y):
        if x + y > y + x:
            return -1
        elif x + y < y + x:
            return 1
        else:
            return 0
    
    # 정렬을 직접 구현
    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if compare(x, pivot) == -1]
        middle = [x for x in arr if compare(x, pivot) == 0]
        right = [x for x in arr if compare(x, pivot) == 1]
        return quicksort(left) + middle + quicksort(right)
    
    sorted_numbers = quicksort(str_numbers)
    
    # 정렬된 숫자들을 이어 붙임
    largest_number = ''.join(sorted_numbers)
    
    # 모든 숫자가 0인 경우 "000..."이 되므로 이때는 "0"을 반환
    if largest_number[0] == '0':
        return '0'
    else:
        return largest_number