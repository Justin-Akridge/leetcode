class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # arr= []
        # for i in letters:
        #     if i is not target and i > target:
        #         arr.append(i)
        # if arr == []:
        #     return letters[0]
        # else:
        #     return min(arr)
        
        l = 0
        r = len(letters)-1
        if target >= letters[-1] or target < letters[0]:
            return letters[0]

        while l <= r:
            mid = (l+r)//2
            if target>=letters[mid]:
                l = mid + 1
            elif letters[mid] > target:
                r = mid -1

        if letters[r] <= target:
            return letters[r+1]
        else:
            return letter[r]
        # if target >= letters[-1] or target < letters[0]:
        #     return letters[0]
        
        # l, r = 0, len(letters) - 1
        # while l <= r:
        #     pivot = (l+r)//2
        #     if target >= letters[pivot]:
        #         l = pivot + 1
        #     elif target < letters[pivot]:
        #         r = pivot - 1

        # if letters[r] <= target:
        #     return letters[r+1]
        
        # else:
        #     return letters[r]