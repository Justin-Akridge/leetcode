class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        if len(s) == 1:
            return False
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stk.append(s[i])
            elif s[i] == ')' or s[i] == '}'  or s[i] == ']':
                if stk == []:
                    return False
                t = stk.pop()
                if s[i] == ')' and t != '(' or s[i] == '}' and t != '{' or s[i] == ']' and t != '[':
                    return False
        return stk == []