class Solution:        
    def climbStairs(self, n: int) -> int:
        numOfWays = 0
        n1, n2 = 0, 1
        num = 0
        while n > 0:
            num = n1 + n2
            numOfWays = num
            n1 = n2
            n2 = num
            n -= 1
        
        return numOfWays
