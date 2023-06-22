class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums)-1

        while l<=r:
            m = int((l+r)/2)
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m-1
            else:
                l = m + 1
        
        return -1
