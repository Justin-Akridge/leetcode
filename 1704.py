class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        arr = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        string1 = s[:len(s) // 2]
        string2 = s[len(s) // 2 if len(s)%2 == 0 else (((len(s)//2))+1):]
        l1 = [x for x in string1]
        l2 = [x for x in string2]
        c1 = 0
        for i in l1:
            if i in arr:
                c1 += 1
        c2 = 0
        for i in l2:
            if i in arr:
                c2 += 1
        return c1 == c2