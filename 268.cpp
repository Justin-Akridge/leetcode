#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    class Solution {
    public:
        int missingNumber(vector<int>& nums) {
            int ans = nums.size();
            int i = 0;
            sort(nums.begin(), nums.end());
            while(i < nums.size()){
                if (nums[i] == i){
                    i += 1;
                }
                else{
                    ans = i;
                    break;
                }
            }
            return ans;
        }
    };
}