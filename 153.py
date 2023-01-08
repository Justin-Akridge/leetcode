class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1
        res = float('inf')

        while l <= r:
            mid = (l + r) // 2
            res = min(res, nums[mid])

            if nums[mid] > nums[r] and nums[r] < nums[l]:
                l = mid + 1

            else:
                r = mid - 1 
        return res
