class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        while left <= right:
            l = [int(x) for x in str(left)]
            sum = 0
            for i in range(len(l)):
                if l[i] != 0 and left % l[i] == 0:
                    sum+=1
            if sum == len(l):
                ans.append(left)
            left+=1
        return ans