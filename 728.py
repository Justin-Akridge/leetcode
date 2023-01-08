def distinctPrimeFactors(nums):
        nums.sort(reverse=True)
        c = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > 1 and nums[i] % 1 == 0 and nums[i] % nums[i] == 0:
                    ans = nums[i] / nums[j]
                    if ans.is_integer():
                        c+=1
                        break
        return c
distinctPrimeFactors([2,4,3,7,10,6])