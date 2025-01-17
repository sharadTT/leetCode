
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        finalNumber = ""

        def factorial(n):
            if n == 1:
                return 1
            return n*factorial(n-1)
        digits = [i for i in range(1,n+1)]
        previousLower = 1


        while n > 0:
            number_range = factorial(n)/n
            i=0
            while i <= n:
                lower_range = number_range*i + previousLower
                upper_range = lower_range + number_range - 1
                if  lower_range <= k <= upper_range:
                    finalNumber = finalNumber+(str(digits[i]))
                    digits.remove(digits[i])
                    previousLower = lower_range
                    break
                i+=1
            n-=1

        return finalNumber

