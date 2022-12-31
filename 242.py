class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create hashmap and add values to it
        d = {}
        for ch in s:
            if ch not in d:
                d[ch]=1
            else:
                d[ch]+=1
                
        # Search hashmap for existing values in string t
        # delete values if values are same
        for ch in t:
            if ch in d:
                if d[ch]>1:
                    d[ch]-=1
                else:
                    del d[ch]
            else:
                return False
        return d == {}