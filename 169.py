class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = {}
        for i in nums:
            if i not in mp:
                mp[i] = 1
            else:
                mp[i] += 1
        print(mp)
        best = 0
        ans = 0
        for i in mp:
            print(mp[i])
            if mp[i] > best:
                best = mp[i]
                ans = i
        return ans