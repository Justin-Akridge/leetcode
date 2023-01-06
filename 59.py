class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        reversed = s[::-1]
        sentence = reversed.strip()
        cnt = 0
        for i in range(len(sentence)):
            if sentence[i] != " ":
                cnt += 1
            else:
                break
        return cnt