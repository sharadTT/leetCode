class Solution(object):
    def productExceptSelf(self, nums):
        length = len(nums)
        prefix_products = [1] * length
        suffix_products = [1] * length
        result = [1] * length

        # Calculate prefix products
        for i in range(1, length):
            prefix_products[i] = prefix_products[i-1] * nums[i-1]

        # Calculate suffix products
        for i in range(length-2, -1, -1):
            suffix_products[i] = suffix_products[i+1] * nums[i+1]

        # Calculate result using prefix and suffix products
        for i in range(length):
            result[i] = prefix_products[i] * suffix_products[i]

        return result
