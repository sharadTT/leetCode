class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 1;
        for k in range(2,int(math.sqrt(2*n))+1):
            if (n - ( k * ( k - 1 )/2)) % k == 0:
                count += 1
                
        return count
