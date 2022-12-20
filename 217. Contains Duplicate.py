class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        newNums = list(set(nums))

        if len(nums) != len(newNums):
            return True
        return False
