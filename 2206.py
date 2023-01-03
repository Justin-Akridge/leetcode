class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums) % 2 == 0:
            for i in range(1, len(nums),+2):
                if nums[i] != nums[i-1]:
                    return False
            return True        
        return False