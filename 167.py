class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(len(numbers)):
            comp = target - numbers[i]
            if comp in hashmap:
                return ([hashmap[comp]+1, i+1])
            else:
                hashmap[numbers[i]] = i
        return hashmap == {}