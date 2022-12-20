class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxNum = len(nums)
        return maxNum*(maxNum+1)//2 - sum(nums)
