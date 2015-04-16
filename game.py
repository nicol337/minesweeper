from minesweeper import Minesweeper
import time
import os

def getLevel():
	levels = ['easy', 'medium', 'hard']
	level = input("Please type "+ ', '.join(levels) + " for level").lower().strip()
	while level not in levels:
		level =  input("Please type "+ ', '.join(levels) + " for level").lower().strip()
	return levels.index(level) * 5 + 5

def main():
	print("Welcome to Minesweeper")
	width = 10
	height = 10
	mine_count = getLevel()
	newGame = Minesweeper(width,height,mine_count)

	gameOver = False
	while not gameOver:

		os.system('clear')
		print("Bombs:",newGame.mine_count,"\t Flags:",newGame.getFlagCount())
		print(newGame)
		row = input("Please enter the row (0 to {0})".format(width))
		while not row.isdigit() or int(row) not in range(width):
			row = input("Please enter the row (0 to {0})".format(width))
		col = input("Please enter the column (0 to {0})".format(height))
		while not col.isdigit() or int(col) not in range(height):
			col = input("Please enter the column (0 to {0})".format(height))
		row = int(row)
		col = int(col)	
		flag = input("Do you want to flag this spot? y/n")
		if flag.lower() == 'y':
			newGame.setFlag(row,col)
		else:
			gameOver = newGame.uncover(row, col) or newGame.isWon()

	newGame.reveal()
	print(newGame)


if __name__ == "__main__":
	main()