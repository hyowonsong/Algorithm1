def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        tmp = bin(arr1[i] | arr2[i])
        # tmp결과 ex) '0b1101'
        
        tmp = tmp[2:].zfill(n)
        # tmp결과 ex) '01101' -> 0b로 나오기 때문에 앞에 2개 제거하고 zfill 사용
        # zfil(n)을 하면 n만큼 부족한 부분을 앞에 0으로 채워준다.
        
        tmp = tmp.replace('1','#').replace('0',' ')
        # 1을 #으로, 0을 공백으로 치환
        
        answer.append(tmp)
    
    return answer