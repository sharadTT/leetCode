from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len > s2_len:
            return False

        s1_counter = Counter(s1)
        window_counter = Counter(s2[:s1_len])

        if window_counter == s1_counter:
            return True

        for i in range(s1_len, s2_len):
            window_counter[s2[i]] += 1
            window_counter[s2[i - s1_len]] -= 1

            if window_counter[s2[i - s1_len]] == 0:
                del window_counter[s2[i - s1_len]]

            if window_counter == s1_counter:
                return True

        return False
