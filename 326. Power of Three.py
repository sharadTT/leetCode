class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        ones = n%10

        if ones not in [1,3,7,9]:
            return False

        i = 0
        while 3**i <= n:
            if 3**i == n:
                return True
            i += 1
        
        return False
