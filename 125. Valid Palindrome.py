class Solution:
    def isPalindrome(self, s: str) -> bool:
        finalStr = ''
        for letter in s:
            # print(letter)
            if letter.isalpha():
                finalStr += letter.lower()
            
            if letter.isnumeric():
                finalStr += letter
                
        #print(finalStr)
        
        if finalStr == finalStr[::-1]:
            return True
        else:
            return False
