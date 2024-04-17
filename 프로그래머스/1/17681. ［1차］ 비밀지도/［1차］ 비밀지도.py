def solution(n, arr1, arr2):
    answer = []
    # arr1과 arr2 겹쳐야하고 전부 2진수로 바꿔줘야 한다.
    for i in range(n):
        tmp = bin(arr1[i]|arr2[i])
        tmp = tmp[2:].zfill(n)
        tmp = tmp.replace('1', '#').replace('0',' ')
        answer.append(tmp)    
    return answer
    