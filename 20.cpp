#include <iostream>
#include <string>
#include <stack>
using namespace std;

class Solution {
public:
  bool isValid(string s) {
    std::stack<char> st;
    for (int i = 0; i < s.size(); i++) {
      switch(s[i]) {
        case '(':
        case '[':
        case '{':
          st.push(s[i]);
          break;
        case ')':
          if (st.empty()) return false;
          if (st.top() == '(') {
            st.pop();
          } else {
            return false;
          }
          break;
        case '}':
          if (st.empty()) return false;
          if (st.top() == '{') {
            st.pop();
          } else {
            return false;
          }
          break;
        case ']':
          if (st.empty()) return false;
          if (st.top() == '[') {
            st.pop();
          } else {
            return false;
          }
          break;
      }
    }
    return st.empty();
  }
};

int main() {
  Solution s;
  bool res = s.isValid("(((({)))))");
  cout << res;
}
