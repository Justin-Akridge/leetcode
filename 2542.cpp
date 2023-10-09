#include <iostream>
#include <vector>
#include <cassert>
#include <climits>
#include <algorithm>

using namespace std;

class Solution {
public:
  void generateSubsets(std::vector<int>& indices, int start, int size_of_vector, 
                       int subsequence_length, std::vector<std::vector<int>>& result) {
    if (subsequence_length == 0) {
      result.push_back(indices);
      return;
    }
    for (int i = start; i < size_of_vector; ++i) {
      indices.push_back(i);
      generateSubsets(indices, i + 1, size_of_vector, subsequence_length - 1, result);
      indices.pop_back();
    }
  }

  std::vector<std::vector<int>> getAllSubsets(int size_of_vector, int subsequence_length) {
    std::vector<std::vector<int>> result;
    std::vector<int> indices;
    generateSubsets(indices, 0, size_of_vector, subsequence_length, result);
    return result;
  }

  long long get_max_subset_value(vector<vector<int>>& subsets, vector<int>& nums1, vector<int>& nums2) {
    long long max_score = 0;
    for (const auto& subset : subsets) {
      long long temp = 0;
      int min_index_value= INT_MAX;
      for (int index : subset) {
        temp += nums1[index]; 
        min_index_value = min(min_index_value, nums2[index]);
      }
      max_score = max(max_score, temp * min_index_value);
    }
    return max_score;
  }

  long long maxScore(vector<int>& nums1, vector<int>& nums2, int subsequence_length) {
    int size_of_vector = nums1.size();
    std::vector<std::vector<int>> subsets = getAllSubsets(size_of_vector, subsequence_length);
    long long max_score = get_max_subset_value(subsets, nums1, nums2);
    return max_score;
  }
};

int main() {
  Solution s1;
  vector<int> nums1 = {1,3,3,2}, nums2 = {2,1,3,4}; 
  int subsequence_length = 3;
  long long ret = s1.maxScore(nums1, nums2, subsequence_length);
  assert(ret == 12);
  nums1 = {4,2,3,1,1}, nums2 = {7,5,10,9,6};
  subsequence_length = 1;
  ret = s1.maxScore(nums1, nums2, subsequence_length);
  assert(ret == 30);
}
