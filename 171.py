class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        sum = 0
        pos = 0
        for i in reversed(columnTitle):
            digit = ord(i) - 64
            sum += (26 ** pos) * digit
            pos += 1
        return sum