class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = nums.count(0)
        
        for i in range(zeroes):
            nums.remove(0)
            
        for i in range(zeroes):
            nums.append(0)
