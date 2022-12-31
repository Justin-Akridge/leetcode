class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #implementing solution with hashset
        hset = set()
        for i in nums:
            if i in hset:
                return True
            else:
                hset.add(i)

        #two pointer
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False        
            