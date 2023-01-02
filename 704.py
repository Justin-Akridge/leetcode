class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums)-1
        low = 0
        while high - low > 1:
            mid = (high + low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        if nums[low] == target:
            return low
        elif nums[high] == target:
            return high
        else:
            return -1