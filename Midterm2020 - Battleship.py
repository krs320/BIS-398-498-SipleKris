# Fairly good, though the program was supposed to 
# generate shots. You have the human both generating the
# shots and calling hits and misses.
###498 Midterm - Battleship Game


import random

Rows = 10
Columns = 10


print("Let's play some battleship!")

#Create Grid
def create_grid(Rows, Columns):
    grid = []
    for row in range(Rows):
        row = []
        for col in range(Columns):
            row.append(' ')
        grid.append(row)
    return grid

grid = create_grid(Rows,Columns)

#Label Grid
def display_grid(grid, Columns):
    column_names = 'abcdefghijklmnopqrstuvwxyz'[:Columns]
    print('  | ' + ' | '.join(column_names.upper()) + ' |')
    for number, row in enumerate(grid):
       print(number + 1, '| ' + ' | '.join(row) + ' |')

grid = create_grid(Rows, Columns)
display_grid(grid, Columns)

#Assign Random Integers
def random_row(grid):
    return random.randint(1,len(grid))

def random_col(grid):
    return random.randint(1,len(grid[0]))

def update_gridHit(grid, GuessRow, GuessColumn):
    grid[GuessRow-1][GuessColumn-1] = 'O'

def update_gridMiss(grid, GuessRow, GuessColumn):
    grid[GuessRow-1][GuessColumn-1] = 'X'

ShipRow = random_row(grid)
ShipColumn = random_col(grid)

#Player Guesses
GuessRow = int(input('What row do you guess? \t'))
GuessColumn = (input('What column do you guess? \t'))
print('Guess =' , GuessColumn,GuessRow )

#Opponent Response
input ( 'Is that a hit? Enter H for hit or N for Miss ' )
response = input

if response == 'H':
    print('You sank my battleship')
	
else:
    print('Splash')
    