class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        #print(a,b)
        
        c=a+b
        c=bin(c)
        return str(c[2:])
