class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = []
        listOfLetter = []
        for letter in s:
            listOfLetter.append(letter)
        limit = pow(2, numRows)
        binary = []
        numbersOfChoice = []
        
        if numRows == 2:
            j=0
        else:
            j=1
        for i in range(j,numRows-1):
            numbersOfChoice.append(pow(2,i))

        numbersOfChoice.sort()
        numbersOfChoice.insert(0,limit-1)
       # print(numbersOfChoice)

        for number in numbersOfChoice:
            binaryNum = '{0:b}'.format(number)
            while len(binaryNum) < numRows:
                binaryNum = '0'+binaryNum
            binary.append(binaryNum)

        newBinary = ''
        for number in binary:
            newBinary += number

        #print(newBinary)
        i=0
        for letter in listOfLetter:
            while newBinary[i] != '1':
                matrix.append('')
                i += 1
                if i >= len(newBinary)-1:
                    matrix.append('')
                    i = 0
            matrix.append(letter)
            i += 1
            if i >= len(newBinary)-1:
                matrix.append('')
                i = 0
        #print(matrix)
        while len(matrix)%numRows != 0:
            matrix.append('')
        #print(matrix)
        matrix = [matrix[i:i+numRows] for i in range(0, len(matrix), numRows)]
       # print(matrix)
        
        finalStr = ''
        for i in range(numRows):
            for j in range(len(matrix)):
                    finalStr+=matrix[j][i]
            
                
        return finalStr
