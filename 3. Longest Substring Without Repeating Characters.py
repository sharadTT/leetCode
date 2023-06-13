class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        max_length = 0
        char_set = set()  # Set to keep track of unique characters
        left, right = 0, 0  # Pointers for the sliding window

        while left < n and right < n:
            if s[right] not in char_set:
                char_set.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                char_set.remove(s[left])
                left += 1

        return max_length
