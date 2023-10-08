#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

class Solution {
public:
  void generateSubsets(std::vector<int>& indices, int start, int n, int k, std::vector<std::vector<int>>& result) {
    if (k == 0) {
      result.push_back(indices);
      return;
    }
    for (int i = start; i < n; ++i) {
      indices.push_back(i);
      generateSubsets(indices, i + 1, n, k - 1, result);
      indices.pop_back();
    }
  }

  std::vector<std::vector<int>> getAllSubsets(int n, int k) {
    std::vector<std::vector<int>> result;
    std::vector<int> indices;

    generateSubsets(indices, 0, n, k, result);

    return result;
  }

  long long maxScore(vector<int>& nums1, vector<int>& nums2, int k) {
    int n = nums1.size();
    std::vector<std::vector<int>> subsets = getAllSubsets(n, k);

    for (const auto& subset : subsets) {
      for (int index : subset) {
          std::cout << index << " ";
      }
      std::cout << "\n";
    }
    return 1;
  }
};

int main() {
  Solution s1;
  vector<int> nums1 = {1,3,3,2}, nums2 = {2,1,3,4}; 
  int k = 3;
  long long ret = s1.maxScore(nums1, nums2, k);
  assert(ret == 12);
}
