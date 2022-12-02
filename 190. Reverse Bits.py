class Solution:
    def reverseBits(self, n: int) -> int:
        binary = format(n, 'b')
        while len(binary)<32:
            binary = '0'+binary
        revStr = binary[::-1]
        return int(revStr, 2)
