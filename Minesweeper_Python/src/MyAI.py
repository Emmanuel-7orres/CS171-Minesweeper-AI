# ==============================CS-199==================================
# FILE:			MyAI.py
#
# AUTHOR: 		Justin Chung
#
# DESCRIPTION:	This file contains the MyAI class. You will implement your
#				agent in this file. You will write the 'getAction' function,
#				the constructor, and any additional helper functions.
#
# NOTES: 		- MyAI inherits from the abstract AI class in AI.py.
#
#				- DO NOT MAKE CHANGES TO THIS FILE.
# ==============================CS-199==================================

from AI import AI
from Action import Action


class MyAI( AI ):

	def __init__(self, rowDimension, colDimension, totalMines, startX, startY):
		self.rowDim = rowDimension
		self.colDim = colDimension
		self.boxes = self.rowDim * self.colDim
		self.totalMines = totalMines
		self.startX = startX
		self.startY = startY
		
		self.board = []
		for i in range(self.rowDim):
			row = []
			for j in range(self.colDim):
				row.append(None)
			self.board.append(row)


		self.mines = set()
		self.safe = set()
		self.uncovered = set()
		for i in range(rowDimension):
			for j in range(colDimension):
				self.uncovered.add((i,j))
		self.covered = set()
		self.covered.add((startX, startY))
		self.mines = set()
		self.actions = []
		self.actionsLoc = []
		self.previousX = startX +1
		self.previousY = startY +1
		self.count = 0

		
	def getAction(self, number: int) -> "Action Object":
		self.count += 1
		print("test count")
		print(self.count)

		# while len(self.actions) != 0:
		# 	return self.actions.pop(0)
		if len(self.mines) == self.totalMines:
			return Action(AI.Action.LEAVE)

		if self.board[self.previousX][self.previousY] == None:
				self.board[self.previousX][self.previousX] = number
				#self.uncovered.remove((self.previousX,self.previousX))
				self.covered.add((self.previousX, self.previousX))

		if number == 0:
			print(self.previousX, self.previousY)
			print("test prev xy")
			neighbors = self.getneighbors(self.previousX,self.previousY)
			for neighbor in neighbors:
					self.actionsLoc.append((neighbor[0], neighbor[1]))
					self.actions.append(Action(AI.Action.UNCOVER, neighbor[0]-1, neighbor[1]-1))

		print("check queue")
		print(self.actionsLoc)
		prevLoc = self.actionsLoc.pop(0)
		self.previousX = prevLoc[0]
		self.previousY = prevLoc[1]
		return self.actions.pop(0)
	
		
		# print("DEBUG")
		# for x, y in self.uncovered:
		# 	#if spot is a mine, go next
		# 	if (x,y) in self.mines:
		# 		continue
			
		# 	neighbors = self.getneighbors(x,y)
		# 	print(neighbors)
		# 	bombs = 0
		# 	for i, j in neighbors:
		# 		if (i,j) in self.mines:
		# 			bombs += 1
			
		# 	if self.board[x][y] == None:
		# 		self.board[x][y] = number
		# 		self.uncovered.remove((x,y))
		# 		return Action(AI.Action.UNCOVER, x, y)
		# 		self.actions.append(Action(AI.Action.UNCOVER))

		# 	elif self.board[x][y] > 0 and self.board[x][y] == bombs:
		# 		for i, j in neighbors:
		# 			if self.board[i][j] == None:
		# 				self.board[i][j] == number
		# 				self.uncovered.remove((i,j))
		# 				return Action(AI.Action.UNCOVER, i, j)
		# 				#self.actions.append(Action(AI.Action.UNCOVER))

		# 	elif len(self.mines) < self.totalMines:
		# 		self.flag_cell(x,y)
		# 		return Action(AI.Action.FLAG, x, y)					

		# # get neighbors
		# # for every valid neighbor, uncover it
		# return Action(AI.Action.LEAVE)
		

	def getneighbors(self, x, z):
		print("check neighbors")
		print(x,z)
		neighbors = set()
		for k in range(x-1, x+2):
			for l in range(z-1, z+2):
				if k!=0 and k <= self.colDim and l != 0 and l <= self.rowDim:
					if (x, z) != (k, l):
						if (k, l) not in self.covered:
							neighbors.add(tuple((k,l)))
		print(neighbors)
		return neighbors

		

	def update_board(self, x, y, val):
		pass

	def flag_cell(self, x, y):
		self.mines.add((x,y))
		#self.actions.append(Action(Ai.Action.FLAG))
		
		
			
