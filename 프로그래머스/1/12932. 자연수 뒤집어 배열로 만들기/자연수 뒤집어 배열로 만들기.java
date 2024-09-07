class Solution {
    public int[] solution(long n){
        // n을 문자열로 바꾼다(long)
        String str = Long.toString(n);

        // 배열의 크기는 문자열의 길이와 동일
        int[] answer = new int[str.length()];

        // 숫자를 위에서부터 하나씩 배열에 저장
        for (int i = 0; i<str.length(); i++){
            answer[i] = Character.getNumericValue(str.charAt(str.length() - 1 - i));
        }

        return answer;
    }
}