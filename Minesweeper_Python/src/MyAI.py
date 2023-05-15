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
		self.totalMines = totalMines
		self.startX = startX
		self.startY = startY
		self.actions = []
		self.neighbors = []
		self.uncovered = set()
		self.board = [[-1 for j in range(self.colDim)] for i in range(self.rowDim)]
		self.mines = set()
		self.start = True	

	def getAction(self, number: int) -> "Action Object":
		while len(self.actions) != 0:
			neighbor = self.neighbors.pop(0)
			if (neighbor[0], neighbor[1]) in self.mines:
				self.uncovered.add((neighbor[0], neighbor[1]))
			else:
				self.uncovered.add((neighbor[0], neighbor[1]))
				self.board[neighbor[0]][neighbor[1]] = number
			return self.actions.pop(0)
		
		if len(self.mines) == self.totalMines:
			return Action(AI.Action.LEAVE)
		
		if self.start == True:
			self.start = False
			self.uncovered.add((self.startX,self.startY))
			self.board[self.startX][self.startY] = number

			if number == 0:
				for i,j in self.get_neighbors(self.startX, self.startY):
					self.actions.append(Action(AI.Action.UNCOVER, i, j))
					self.neighbors.append((i,j))
			return self.actions.pop(0)
		else:

			neighbor = self.neighbors.pop(0)
			#print("Tile Uncovered (Index): ", neighbor)
			self.uncovered.add((neighbor[0], neighbor[1]))
			self.board[neighbor[0]][neighbor[1]] = number

			for i,j in self.uncovered:
				if self.board[i][j] == 0:
					for t,k in self.get_neighbors(i, j):
						self.actions.append(Action(AI.Action.UNCOVER, t, k))
						self.neighbors.append((t,k))
			

				elif self.board[i][j] != "B" and self.board[i][j] > 0:
					uncovered_neighbors = [(t,k) for t,k in self.get_neighbors(i, j) if self.board[t][k] == -1]
					flagged_neighbors = [(t,k) for t,k in self.get_neighbors(i, j) if self.board[t][k] == "B"]

					if len(uncovered_neighbors) == self.board[i][j] - len(flagged_neighbors):
						for t,k in uncovered_neighbors:
							self.actions.append(Action(AI.Action.FLAG, t, k))
							self.neighbors.append((t,k))
							self.board[t][k] = "B"
							self.mines.add((t,k))
					elif self.board[i][j] == len(flagged_neighbors):
						for t,k in uncovered_neighbors:
							self.actions.append(Action(AI.Action.UNCOVER, t, k))
							self.neighbors.append((t,k))
							
			for i ,j in self.uncovered:
				count = 0
				if self.board[i][j] != "B" and self.board[i][j] > 0:
					neighbors = set()
					for k in range(i-1, i+2):
						for t in range(j-1, j+2):
							if k >= 0 and k < self.rowDim and t >= 0 and t < self.colDim:
								if (k, t) != (i, j):
									neighbors.add((k, t))

					for neighbor in neighbors:
						if neighbor in self.mines and self.board[neighbor[0]][neighbor[1]] != -1:
							count += 1
					if count == self.board[i][j]:
						for neighbor in neighbors:
							if neighbor not in self.uncovered:
								self.actions.append(Action(AI.Action.UNCOVER, i, j))
								self.neighbors.append((i,j))
				else:
					continue
			return self.actions.pop(0)
		
		return Action(AI.Action.LEAVE)
		
	def get_neighbors(self, x, y):
		neighbors = set()
		for i in range(x-1, x+2):
			for j in range(y-1, y+2):
				if i >= 0 and i < self.rowDim and j >= 0 and j < self.colDim:
					if (x, y) != (i, j) and (i, j) not in self.uncovered:
						neighbors.add((i, j))
		#print("Neighbors of (index)", (x,y), " : ", neighbors)
		return neighbors
	
	def printBoard(self):
		for arr in self.board:
			print(arr)
	