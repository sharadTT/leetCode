class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        for i,letter in enumerate(reversed(columnTitle)):
            if i == 0:
                num += ord(letter)-64
            else:
                num += (26**i)*(ord(letter)-64)
            
        return num
