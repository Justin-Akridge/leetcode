#include <iostream>

class Solution {
  public:
    int hammingWeight(uint32_t n) {
      int ans = 0;
      uint32_t temp = n;

      while (temp) {
        if (temp % 2 == 1) {
          ++ans;
        }
        temp /= 2;
      }
      return ans;
    }
};

