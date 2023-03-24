class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        i = 0
        while i < len(nums1):
            arr.append(nums1[i])
            i+=1
        i = 0
        while i < len(nums2):
            arr.append(nums2[i])
            i+=1
        arr.sort()
        i = 0
        j = len(arr)-1
        if(len(arr)-1 % 2 == 0):
            ans = arr[len(arr)//2]
            return ans / 1.0
        else:
            while(i < j):
                i+=1
                j-=1
        return (arr[i] + arr[j]) / 2.0