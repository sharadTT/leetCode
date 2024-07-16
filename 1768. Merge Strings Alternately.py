class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newStr = ""

        len1 = len(word1)
        len2 = len(word2)

        maxLength = len1 if len1>=len2 else len2

        use1, use2 = False, False
        if len1 > 0:
            use1 = True
        if len2 > 0:
            use2 = True
        i=-1
        while i < maxLength:
            i+=1
            if i >= len1:
                use1 = False
            if i >= len2:
                use2 = False

            if use1:
                newStr += word1[i]

            if use2:
                newStr += word2[i]
        
        return newStr
