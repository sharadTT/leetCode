class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        thisDict = {}
        
        for num in nums:
            if num not in thisDict:
                thisDict[num] = 1
            else:
                thisDict[num] += 1
                
        for key, value in thisDict.items():
            if value > len(nums)//2:
                return key
            
        return -1
