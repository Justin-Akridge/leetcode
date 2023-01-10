class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      for i in nums:
        if nums.count(i) == 1:
          return i
singleNumber([2,2,1])

##map

mp = {}
  for i in nums:
    if i not in mp:
      mp[i] = 1
    else:
      mp[i] +=1
    for i in mp:
      if mp[i] == 1:
  return i