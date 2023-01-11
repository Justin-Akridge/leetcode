class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hashmap:
                return [i, hashmap[compliment]]
            hashmap[nums[i]] = i

#cpp solution
# class Solution {
# public:
#     vector<int> twoSum(vector<int>& nums, int target) {
#         unordered_map<int, int> mp;
#         vector<int> result;
#         for(int i=0; i<nums.size(); i++){
#             int complement = target - nums[i];
#             if (mp.find(complement) != mp.end()){
#                 result.push_back(mp[complement]);
#                 result.push_back(i);
#                 break;
#             } else{
#                 mp.insert({nums[i], i});
#             }
#         }
#         return result;
#     }
# };