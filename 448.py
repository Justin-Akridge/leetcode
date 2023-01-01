class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i]=True
        ans = []
        for i in range(1, len(nums)+1):
            if i not in hashmap:
                ans.append(i)
        return ans
findDisappearedNumbers([4,3,2,7,8,2,3,1])