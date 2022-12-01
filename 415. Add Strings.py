class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        number1 = ''
        number2 = ''
        for digit in num1:
            number1 += str(digit)
        
        for digit in num2:
            number2 += str(digit)
        
        number = int(number1) + int(number2)
        #print(number)
        
        return str(number)
