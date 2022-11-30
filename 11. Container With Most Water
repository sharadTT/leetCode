class Solution:
    def maxArea(self, height: list[int]) -> int:
        maximum = 0
        i = 0
        j = len(height)-1
        
        while i<j:
            area = abs(i-j)*min(height[i],height[j])
            if area >= maximum:
                maximum = area
            if height[i] < height[j]:
                i += 1
            else:
                j -=1

        return maximum
