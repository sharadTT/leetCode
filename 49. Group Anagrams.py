class Solution(object):
    def groupAnagrams(self, strs):
        dict = {}

        for word in strs:
            sortedWord = ''.join(sorted(word))

            if sortedWord not in dict:
                dict[sortedWord] = []

            dict[sortedWord].append(word)

        return list(dict.values())
