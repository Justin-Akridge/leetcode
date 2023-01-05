class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        e = ""
        for i in s:
            if i.isalpha() or i.isnumeric():
                e+=i
        rs = ""
        i=0
        j=len(e)-1
        while i<j:
            if e[i] != e[j]:
                return False
            else:
                i+=1
                j-=1
        return True