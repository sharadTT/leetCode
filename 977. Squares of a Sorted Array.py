class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        finalList = [num**2 for num in nums]
        finalList.sort()
        return finalList
