#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

class Solution {
public:
  int binary_search(vector<int>& nums, int target, bool left) {
    int index = -1;
    int low = 0;
    int high = nums.size() - 1;
    while (low <= high) {
      int mid = low + ((high - low) / 2);
      if (nums[mid] == target) {
        index = mid;
        if (left)
          high = mid - 1;
        else
          low = mid + 1;
      } else if (nums[mid] < target) {
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }
    return index;
  }

  vector<int> searchRange(vector<int> nums, int target) {
    vector<int> range = {-1, -1};
    range[0] = binary_search(nums, target, true);
    range[1] = binary_search(nums, target, false); 
    return range;
  }
};

int main() {
  Solution s;
  vector<int> results = s.searchRange({5,7,7,8,8,10}, 8);
  vector<int> ans = {3, 4};

  for (int i = 0; i < results.size(); i++) {
    assert(results[i] == ans[i]);
  }
  
  results = s.searchRange({5,7,7,8,8,10}, 6);
  ans = {-1,-1};
  for (int i = 0; i < results.size(); i++) {
    assert(results[i] == ans[i]);
  }

  results = s.searchRange({}, 0);
  ans = {-1,-1};
  for (int i = 0; i < results.size(); i++) {
    assert(results[i] == ans[i]);
  }
}
