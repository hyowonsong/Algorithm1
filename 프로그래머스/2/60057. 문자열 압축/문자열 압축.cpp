#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    int answer = s.length();  // 초기 답은 문자열의 길이로 초기화합니다.

    for (int i = 1; i <= s.length() / 2; ++i) {
        int pos = 0;            // 현재 압축을 시작할 위치를 나타냅니다.
        int length = s.length(); // 현재 압축된 문자열의 길이를 나타냅니다.

        // 현재 압축 단위로 문자열을 확인합니다.
        while (pos + i <= s.length()) {
            string unit = s.substr(pos, i);  // 압축 단위의 부분 문자열을 가져옵니다.
            pos += i;                        // 현재 단위 길이만큼 위치를 이동합니다.

            int cnt = 0; // 반복되는 부분 문자열의 개수를 세기 위한 변수입니다.

            // 현재 압축 단위로 반복되는 부분 문자열의 개수를 세줍니다.
            while (pos + i <= s.length()) {
                if (unit == s.substr(pos, i)) {
                    cnt += 1;
                    pos += i;
                } else {
                    break;
                }
            }

            // 만약 압축이 발생했다면 압축된 길이를 업데이트합니다.
            if (cnt > 0) {
                length -= i * cnt;

                // 압축된 횟수에 따라 길이를 조정해줍니다.
                if (cnt < 9) {
                    length += 1;
                } else if (cnt < 99) {
                    length += 2;
                } else if (cnt < 999) {
                    length += 3;
                } else {
                    length += 4;
                }
            }
        }

        // 현재까지의 최소 길이를 업데이트합니다.
        answer = min(answer, length);
    }

    return answer;
}
