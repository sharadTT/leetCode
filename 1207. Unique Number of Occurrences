class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        thisDict = {}
        
        for num in arr:
            if num in thisDict:
                thisDict[num] += 1
            else:
                thisDict[num] = 1
        
        rev_dict = {}
  
        for key, value in thisDict.items():
            rev_dict.setdefault(value, set()).add(key)
      
        result = [key for key, values in rev_dict.items() if len(values) > 1]
        
        if result == []:
            return True
        else:
            return False
