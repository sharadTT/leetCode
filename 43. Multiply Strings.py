class Solution:
    def convertStringToInt(s): 
        num = 0
        for i in s:
            num = num * 10 + (ord(i) - 48) 
        return num
    
    def convertIntToString(num):
        numStr = ''
        while num > 0:
            digit = num%10
            num //=10
            numStr += str(digit)
        numStr = numStr[::-1]
        return numStr
    
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        product = Solution.convertStringToInt(num1) * Solution.convertStringToInt(num2)
        return Solution.convertIntToString(product)
