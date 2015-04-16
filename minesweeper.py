from tile import Tile
import random

class Minesweeper:
	def __init__(self, width, height, mineCount):
		self.board = []
		self.width = width
		self.height = height
		self.mineCount = mineCount

		for i in range(width):
			for j in range(height):
				self.board.append(Tile(i,j))

		self.__setMines()
		self.__setNumbers()

	def __setMines(self):
		random.shuffle(self.board)
		for i in range(self.mineCount):
			self.board[i].setMine()

	def __setNumbers(self):
		neighbors_index = (-1,0,1)
		for tile in self.board:
			if tile.value != 9:
				for i in neighbors_index:
					for j in neighbors_index:
						if tile.x+i in range(0,self.width) and tile.y+j in range(0,self.height):
							if (self.getTile(tile.x+i, tile.y+j).isMine()):
								tile.value+=1

	def reveal(self):
		for tile in self.board:
			tile.setVisited()

	def getFlagCount(self):
		count = 0
		for tile in self.board:
			if tile.isFlagged():
				count+=1
		return count

	def visit(self, x, y):
		self.board[x][y].setVisited()
		self.uncover(x,y)

	def setFlag(self, x, y):
		self.getTile(x,y).setFlag()

	def uncover(self, x, y):
		tile = self.getTile(x,y)
		if tile.isMine():
			print("You Lost!")
			return True
		tile.setVisited()
		neighbors_index = (-1,0,1)
		tiles = [tile]

		while not tiles == []:
			
			tile = tiles.pop()
			if tile.isBlank():
				for i in neighbors_index:
					for j in neighbors_index:
						if tile.x+i in range(self.width) and tile.y+j in range(self.height):
							neighbor = self.getTile(tile.x+i, tile.y+j)
							if not neighbor.isVisited() and neighbor != tile:
								neighbor.setVisited()
								tiles.append(neighbor)
		return False

	def isWon(self):
		for tile in self.board:
			if not tile.isVisited() and not tile.isMine():
				return False
		print("You Won!")
		return True

	def getTile(self, x, y):
		for tile in self.board:
			if tile.x == x and tile.y == y:
				return tile

	def __str__(self):
		board_str = '   '+' '.join([str(x)+' ' for x in range(self.width)])+'\n'
		for i in range(self.width):
			board_str+=str(i)+' '
			for j in range(self.height):
				tile = self.getTile(i,j)
				board_str += ' '+str(tile)+' '
			board_str+='\n'
		return board_str





