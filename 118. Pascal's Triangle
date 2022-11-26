class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a = []

        for i in range(numRows):
            inner = [None]*(i+1)
            j=0
            while j <= i:
                if j == 0 or j == i:
                    inner[j] = 1
                else:
                    inner[j] = a[i-1][j] + a[i-1][j-1]
                j += 1
            a.append(inner)
        
        return a
