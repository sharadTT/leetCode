class Solution(object):
    def longestConsecutive(self, nums):
        nums = sorted(nums)
        longest_sublist = []
        current_sublist = []
    
        for num in nums:
            if not current_sublist:
                current_sublist.append(num)
            elif num == current_sublist[-1] + 1:
                current_sublist.append(num)
            elif num == current_sublist[-1]:
                continue
            else:
                if len(current_sublist) > len(longest_sublist):
                    longest_sublist = current_sublist
                current_sublist = [num]
    
        if len(current_sublist) > len(longest_sublist):
            longest_sublist = current_sublist

        return len(longest_sublist)
