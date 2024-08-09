# 뉴스 클러스터링(자카드 유사도)
# 자카드 유사도는 다중집합(2글자씩 끊어서 사용하기 때문에 끊어줘야한다.)
# 두 집합의 교집합 크기/ 두 집합의 합집합 크기

from collections import Counter
# Counter는 딕셔너리 형태로 요소의 개수를 셀 수 있게 해준다.

# 다중집합 만들기 함수
def make_multiset(string):
    # 딕셔너리 형태로 만들어준다.
    multiset = Counter()                  
    for i in range(len(string) - 1):
        # 영문자로 된 글자 쌍만 유효
        if string[i:i+2].isalpha():  
            multiset[string[i:i+2]] += 1
    return multiset

def solution(str1, str2):
    # 대소문자 구분 없이 처리하기 위해 모두 소문자로 변환
    str1 = str1.lower()
    str2 = str2.lower()
    
    # 다중집합 만들기
    multiset1 = make_multiset(str1)
    multiset2 = make_multiset(str2)
    
    # Counter 클래스를 사용하여 교집합과 합집합 계산
    intersection = sum((multiset1 & multiset2).values())
    union = sum((multiset1 | multiset2).values())
    
    # 자카드 유사도 계산
    if union == 0:  # 합집합이 공집합인 경우
        jaccard_similarity = 1
    else:
        jaccard_similarity = intersection / union
    
    # 정수부분만 출력하기 위해 65536을 곱하고 버림
    answer = int(jaccard_similarity * 65536)
    
    return answer