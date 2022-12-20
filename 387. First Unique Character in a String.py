class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        for i,letter in enumerate(s):
            if letter not in s[i+1:] and letter not in seen:
                return i
            seen.add(letter)
        return -1
