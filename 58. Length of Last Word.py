class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        listOfWords = s.split(" ")
        while("" in listOfWords):
            listOfWords.remove("")
        return (len(listOfWords[len(listOfWords)-1]))
