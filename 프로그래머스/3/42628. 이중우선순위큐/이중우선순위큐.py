from heapq import heapify, heappush, heappop

def solution(operations):
    answer = []
    hq = []                 # heapq 저장할 리스트

    for operation in operations:
        alphabet, number = operation.split()    # operations 나누기
        number = int(number)

        if alphabet == 'I' :       # I면 삽입이니까 heappush
            heappush(hq, number)
        else: # alphabet == 'D'        # I가 아니면 
            if hq:
                if number == -1:
                    heappop(hq) # 최솟값을 삭제
                else:
                    hq.sort()
                    hq.pop() # 최댓값을 삭제

    # 모든 연산을 처리한 후
    hq.sort()
    if hq: # 큐가 비어있지 않음
        answer = [hq[-1], hq[0]]
    else:
        answer = [0,0]

    return answer