class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0){
            return false;
        }
        vector<int> sd;
        while(x){
            int digit = x % 10;
            x/=10;
            sd.push_back(digit);
            
        }
        int j = sd.size()-1;
        for(int i=0; i<sd.size(); i++){
            if (sd[i] != sd[j]){
                return false;
            }
            j--;
        }
        return true;
    }
};
