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
		self.flagged = set()


		
	def getAction(self, number: int) -> "Action Object":
		if number == 0:
			pass

		if len(self.mines) == self.totalMines:
			return Action(Action.LEAVE)
		if len(self.board) == self.boxes:
			return Action(Action.LEAVE)
		
		

	def getneighbors(self, i, j):
		pass

	def update_board(self, x, y, val):
		pass

	def flag_cell(self, x, y):
		pass
			
