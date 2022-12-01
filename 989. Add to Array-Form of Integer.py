class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        number = ''
        for digit in num:
            number += str(digit)
        
        number = int(number) + k
        #print(number)
        
        finalList = []
        while number > 0:
            digit = number%10
            number = number//10
            finalList.append(digit)
        finalList.reverse()
        
        return finalList
