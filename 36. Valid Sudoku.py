class Solution(object):
    def isValidSudoku(self, board):
        for row in board:
            temp = [i for i in row if i != '.']
            if len(temp) != len(set(temp)):
                return False
            
        transposed_board = [list(row) for row in zip(*board)]

        for row in transposed_board:
            temp = [i for i in row if i != '.']
            if len(temp) != len(set(temp)):
                return False
            
        three_by_three_boards = []

        # Iterate over the rows in steps of 3
        for i in range(0, 9, 3):
            # Iterate over the columns in steps of 3
            for j in range(0, 9, 3):
                # Extract the elements for the current 3x3 board
                three_by_three_board = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                # Append the 3x3 board to the temp
                three_by_three_boards.append(three_by_three_board)

        for row in three_by_three_boards:
            temp = [i for i in row if i != '.']
            if len(temp) != len(set(temp)):
                return False      
        
        return True
