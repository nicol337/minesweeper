class Tile:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.value = 0
		self.status = 'covered'

	def setMine(self):
		self.value = 9
	
	def isMine(self):
		return self.value == 9

	def setVisited(self):
		self.status = 'uncovered'

	def isBlank(self):
		return self.value == 0

	def isVisited(self):
		return self.status == 'uncovered'

	def isFlagged(self):
		return self.status == 'flagged'

	def setFlag(self):
		if self.status == 'covered':
			self.status = 'flagged'
		elif self.status == 'flagged':
			self.status = 'covered'

	def __str__(self):
		if self.status == 'flagged':
			return ">"
		elif self.status == 'covered':
			return "-"
		elif self.value == 9:
			return '*'
		elif self.value == 0:
			return ' '
		else:
			return str(self.value)
