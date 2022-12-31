class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      #implementing solution with hashset
        hset = set()
        for i in nums:
            if i in hset:
                return True
            else:
                hset.add(i)
            