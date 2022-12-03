class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        thisDict = {}
        for num in nums:
            if num not in thisDict:
                thisDict[num] = 1
            else:
                thisDict[num] += 1
        
        finalList = []
        while k >0:
            maxNum = max(thisDict, key=thisDict.get)
            finalList.append(maxNum)
            del thisDict[maxNum]
            k -= 1
                
        return finalList
