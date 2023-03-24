class Solution:
    def reverse(self, x: int) -> int:
        def sign(x):
            if x >= 0:
                return 1
            else:
                return -1
        sign = sign(x)
        rev = str(abs(x))
        rev = int(rev[::-1])
        ans = (sign*rev)
        if (ans > 2 ** 31 - 1 or ans < -2 ** 31): 
            return 0
        return ans