import random
from four_Line import column_winner


def victory_column(board,ficha):
        first_row = 0
        column = 0
        board = board
        
        while column <= 7:
            for row in board:
                if (board[first_row][column] == ficha) and (board[first_row + 1][column] == ficha) and (board[first_row + 2][column] == ficha) and (board[first_row + 3][column] == ficha):
                    winner = True 
                    return winner
                if first_row == 4:
                    first_row = 0
                    break
                first_row += 1
            column += 1 
        
#Contruccion de tablero
board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]  

a = column_winner(board,'x')
print(a)
