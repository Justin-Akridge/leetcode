    #include <iostream>
    #include <string>
    using namespace std;
    string lengthOfLastWord(string s) {
        int start = 0;
        int end = s.length()-1;
        string trimmed_string;
        for(int i=0; i<=end; i++){
            if(s[i] != ' '){
                start = i; break;
            }
        }
        for(int i=end; i>=0; i--){
            if(s[i] != ' '){
                end = i;
                break;
            }
        }
        for(int i=start; i<=end; i++){
            trimmed_string += s[i];
        }  
        return trimmed_string;
    }

    int main(){
        string str;
        str = "     I love c++ programming.      ";
        cout << lengthOfLastWord(str);
    }