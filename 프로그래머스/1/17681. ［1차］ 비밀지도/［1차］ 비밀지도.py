def solution(n, arr1, arr2):
    answer = []
    # arr1과 arr2의 각 요소를 비트 OR 연산으로 결합하고, 결과를 2진수로 변환
    for i in range(n):
        tmp = bin(arr1[i] | arr2[i])
        # 2진수 문자열에서 '0b'를 제거하고 n자리로 채우기(2진수이기 때문에 아무리커도 1)
        tmp = tmp[2:].zfill(n)
        # '1'을 '#'으로, '0'을 ' '으로 변환
        tmp = tmp.replace('1', '#').replace('0', ' ')
        # 변환된 문자열을 결과 리스트에 추가
        answer.append(tmp)
    return answer