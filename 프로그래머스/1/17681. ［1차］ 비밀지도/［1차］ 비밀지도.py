def solution(n, arr1, arr2):
    answer = []
    
    # n 자리만큼의 행을 만들어야
    for i in range(n):
        # arr1과 arr2 각 요소를 비트 OR 연산으로 결합, 결과를 2진수로 변환
        tmp = bin(arr1[i] | arr2[i])
        # 2진수 문자열에서 '0b'를 제거하고 n자리만큼 0으로 채우기(zfill)
        tmp = tmp[2:].zfill(n)
        # '1'을 '#'으로, '0'을 ' '으로 변환
        tmp = tmp.replace('1', '#').replace('0', ' ')
        # 변환된 문자열을 결과 리스트에 추가
        answer.append(tmp)
    return answer