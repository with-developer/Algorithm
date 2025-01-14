#include <iostream>
#include <string>
using namespace std;

string isSubsequence(string s, string t) {
    int s_len = s.length();
    int t_len = t.length();
    int s_idx = 0;
    
    // s의 각 문자에 대해
    for(int t_idx = 0; t_idx < t_len && s_idx < s_len; t_idx++) {
        // 현재 위치의 문자가 일치하면 s의 다음 문자로 이동
        if(s[s_idx] == t[t_idx]) {
            s_idx++;
        }
    }
    
    // s의 모든 문자를 찾았는지 확인
    return (s_idx == s_len) ? "Yes" : "No";
}

int main() {
    string s, t;
    
    // EOF까지 입력 받기
    while(cin >> s >> t) {
        cout << isSubsequence(s, t) << endl;
    }
    
    return 0;
}