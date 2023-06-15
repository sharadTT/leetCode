class Solution(object):
    def isHappy(self, n):
        numIncluded = []
        while n > 0:    
            currentNumber = n
            sqSum = 0
            while currentNumber > 0:
                digit = currentNumber % 10
                currentNumber = int(currentNumber / 10)

                sqSum += digit**2
            if sqSum == 1:
                return True
            else:
                n = sqSum
                if n in numIncluded:
                    return False
                else:
                    numIncluded.append(n)
                
        return False
