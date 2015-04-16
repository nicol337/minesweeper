from tile import Tile
import random

class Minesweeper:
	def __init__(self, width, height, mine_count):
		self.board = []
		self.width = width
		self.height = height
		self.mine_count = mine_count

		for i in range(width):
			for j in range(height):
				self.board.append(Tile(i,j))

		self.__setMines()
		self.__setNumbers()

	def __setMines(self):
		mines_placed = 0
		while mines_placed != self.mine_count:
			row = random.randint(0,self.width-1)
			col = random.randint(0,self.height-1)
			tile = self.getTile(row,col)
			if not tile.isMine():
				tile.setMine()
				mines_placed += 1

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
		tile_index = x*self.width + y
		return self.board[tile_index]

	def __str__(self):
		board_str = '   '+' '.join([str(x)+' ' for x in range(self.width)])+'\n'
		for i in range(self.width):
			board_str+=str(i)+' '
			for j in range(self.height):
				tile = self.getTile(i,j)
				board_str += ' '+str(tile)+' '
			board_str+='\n'
		return board_str





