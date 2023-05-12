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
		self.mines = set()
		self.actions = []


		
	def getAction(self, number: int) -> "Action Object":


		while len(self.actions) != 0:
			return self.actions.pop(0)
		
		if len(self.mines) == self.totalMines:
			return Action(AI.Action.LEAVE)
		if len(self.board) == self.boxes:
			return Action(AI.Action.LEAVE)
		
		for x, y in self.board:
			#if spot is a mine, go next
			if (x,y) in self.mines:
				continue
			
			neighbors = self.getneighbors(x,y)
			print(neighbors)
			bombs = 0
			for i, j in neighbors:
				if (i,j) in self.mines:
					bombs += 1
			

			if self.board[x][y] == None:
				return Action(AI.Action.UNCOVER, x, y)
				#self.actions.append(Action(AI.Action.UNCOVER))

			elif self.board[x][y] > 0 and self.board[x][y] == bombs:
				for i, j in neighbors:
					if self.board[i][j] == None:
						return Action(AI.Action.UNCOVER, i, j)
						#self.actions.append(Action(AI.Action.UNCOVER))

			elif len(self.mines) < self.totalMines:
				self.flag_cell(x,y)
				return Action(AI.Action.FLAG, x, y)					

		# get neighbors
		# for every valid neighbor, uncover it
		return Action(AI.Action.LEAVE)
		

	def getneighbors(self, i, j):
		neighbors = set()
		for k in range(i-1, i+2):
			for l in range(j-1, j+2):
				if k!=0 and k <= self.columnDim and l != 0 and l <= self.rowDim:
					if (i, j) != (k, l):
						neighbors.add(tuple((k,l)))
		return neighbors

		

	def update_board(self, x, y, val):
		pass

	def flag_cell(self, x, y):
		self.mines.add((x,y))
		#self.actions.append(Action(Ai.Action.FLAG))
		
		
			
