class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        finalList = []
        
        i = n
        while i > 0:
            if i % 15 == 0:
                finalList.append('FizzBuzz')
            elif i % 5 == 0:
                finalList.append('Buzz')
            elif i % 3 == 0:
                finalList.append('Fizz')
            else:
                finalList.append(str(i))
            i -= 1
                
        finalList = finalList[::-1]
        return finalList
