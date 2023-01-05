#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int count = 0;
        for(auto x: jewels){
            for(auto c: stones){
                if(c==x){
                    count++;
                }
            }
        }
        return count;
    }
};