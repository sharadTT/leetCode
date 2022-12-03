class Solution:
    def frequencySort(self, s: str) -> str:
        thisDict = {}
        for letter in s:
            if letter not in thisDict:
                thisDict[letter] = 1
            else:
                thisDict[letter] += 1
                
        finalWord = ''
        while len(thisDict) > 0:
            maxLetter = max(thisDict, key=thisDict.get)
            while thisDict[maxLetter] > 0:
                finalWord += maxLetter
                thisDict[maxLetter] -= 1
            del thisDict[maxLetter]
        
        print(finalWord)
        return finalWord
