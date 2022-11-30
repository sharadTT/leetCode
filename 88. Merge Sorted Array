class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if nums2 == []:
            return None
        
        if nums1 == []:
            nums1 = nums2
            return None
        
        for i in range(m,m+n):
            nums1[i] = nums2[i-m]
            
        nums1.sort()
