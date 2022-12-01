class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        vowels1 = 0
        vowels2 = 0
        lengthOfS = len(s)
        for i in range(lengthOfS//2):
            if s[i] in vowels:
                vowels1 += 1
            if s[i+lengthOfS//2] in vowels:
                vowels2 += 1
        if vowels1 == vowels2:
            return True
        else:
            return False
