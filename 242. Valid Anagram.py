class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        listS = []
        listT = []

        for letter in s:
            listS.append(letter)
        for letter in t:
            listT.append(letter)
        listS.sort()
        listT.sort()

        if listS == listT:
            return True
        else:
            return False
