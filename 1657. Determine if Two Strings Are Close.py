class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        oneDict = {}
        twoDict = {}
        
        for letter in word1:
            if letter in oneDict:
                oneDict[letter] += 1
            else:
                oneDict[letter] = 1
        
        for letter in word2:
            if letter in twoDict:
                twoDict[letter] += 1
            else:
                twoDict[letter] = 1
                
        #print(oneDict, twoDict)
        
        valuesOne = [value for value in oneDict.values()]
        keysOne = [key  for key in oneDict.keys()]
        
        valuestwo = [value for value in twoDict.values()]
        keysTwo = [key  for key in twoDict.keys()]
        
        valuesOne.sort()
        valuestwo.sort()
        keysOne.sort()
        keysTwo.sort()
        
        #print(valuesOne,valuestwo)
        #print(keysOne, keysTwo)
        
        if valuesOne == valuestwo and keysOne == keysTwo:
            return True
        else:
            return False
