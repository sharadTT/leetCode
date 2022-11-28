class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        while l <= r:
            mid = l + (r-l)//2
            if mid * mid == num:
                return True
            elif mid * mid <= num < (mid+1)*(mid+1):
                return False
            elif num < mid * mid:
                r = mid - 1
            else:
                l = mid + 1
