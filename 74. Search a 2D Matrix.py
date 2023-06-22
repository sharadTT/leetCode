class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        colummns = len(matrix[0])

        for line in matrix:
            if target >= line[0] and target <= line[len(matrix[0])-1]:
                nums = line
                l = 0
                r = len(nums)-1

                while l<=r:
                    m = int((l+r)/2)
                    if nums[m] == target:
                        return True
                    elif nums[m] > target:
                        r = m-1
                    else:
                        l = m + 1
        return False
