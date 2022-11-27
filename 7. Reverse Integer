class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            sign = 1
        else:
            sign = -1
        
        x *= sign
        
        reversed_num = 0

        while x != 0:
                digit = x % 10
                reversed_num = reversed_num * 10 + digit
                x //= 10
                
        if reversed_num > -2147483648 and reversed_num < 2147483647:
            return reversed_num*sign
        else:
            return 0
