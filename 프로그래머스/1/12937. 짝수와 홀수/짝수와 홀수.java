class Solution {
    // String 반환
    public String solution(int num){
        String answer = "";

        if (num % 2 != 0) {
            answer += "Odd";
        } else {
            answer += "Even";
        }

        return answer;
    }
}