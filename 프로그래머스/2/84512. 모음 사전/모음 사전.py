from itertools import product

def solution(word):
    answer = []  # 단어들을 저장할 리스트
    
    li = ['A', 'E', 'I', 'O', 'U']  # 사용할 알파벳 모음 리스트
    
    # 길이가 1부터 5까지의 모든 조합 생성하여 answer에 저장
    for i in range(1, 6):
        # product를 사용하여 알파벳 모음에서 길이 i의 모든 조합 생성
        for per in product(li, repeat=i):
            answer.append(''.join(per))  # 생성된 조합을 문자열로 변환하여 리스트에 추가
    
    answer.sort()  # 사전 순서대로 정렬
    
    # 주어진 단어 word가 정렬된 리스트 answer에서 몇 번째 위치하는지 반환
    return answer.index(word) + 1  # 인덱스는 0부터 시작하므로 +1을 해서 1부터 시작하는 위치로 변환
