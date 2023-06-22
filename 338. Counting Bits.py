class Solution(object):
    def count_bits(self, number):
        count = 0
        while number != 0:
            count += number & 1
            number >>= 1
        return count

    def countBits(self, n):
        lst = []
        for i in range(n+1):
            lst.append(self.count_bits(i))
        
        return lst
