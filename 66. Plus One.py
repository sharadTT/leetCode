class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        numStr = ''
        for num in digits:
            numStr += str(num)
        
        numStr = int(numStr) + 1
        
        finalList = []
        while numStr > 0:
            digit = numStr%10
            numStr = numStr//10
            finalList.append(digit)
        finalList.reverse()
        
        return finalList
