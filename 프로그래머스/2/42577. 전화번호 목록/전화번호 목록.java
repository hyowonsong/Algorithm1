import java.util.Arrays;

class Solution {
    // 한 번호가 다른 번호의 접두어인 경우 false
    // 아니면 true
    public boolean solution(String[] phone_book) {
        // 1. 전화번호부 정렬
        Arrays.sort(phone_book);

        // 2. 전화번호부에서 연속된 두 개의 전화번호 비교
        for (int i = 0; i < phone_book.length - 1; i++) {
            // phone_book[i+1] 문자열이 phone_book[i] 문자열로 시작하는지를 확인
            if (phone_book[i + 1].startsWith(phone_book[i]))
                return false;
        }
        return true;
    }
}