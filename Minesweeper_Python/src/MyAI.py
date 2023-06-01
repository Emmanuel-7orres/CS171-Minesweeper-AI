from collections import deque
from AI import AI
from Action import Action

class MyAI(AI):
    def __init__(self, rowDimension, colDimension, totalMines, startX, startY):
        self.rowDim = rowDimension
        self.colDim = colDimension
        self.totalMines = totalMines
        self.startX = startX
        self.startY = startY
        self.actions = deque()
        self.neighbors = deque()
        self.uncovered = set()
        self.board = [[-2] * self.colDim for _ in range(self.rowDim)]
        self.mines = set()
        self.start = True

    def getAction(self, number: int) -> "Action Object":
        if len(self.mines) == self.totalMines:
            #print("ALL MINES FOUND, UNCOVERING BOARD\n")
            for i in range(self.colDim):
                for j in range(self.rowDim):
                    if self.board[i][j] == -2 and (i,j) not in self.mines:
                        self.actions.append(Action(AI.Action.UNCOVER, i, j))
            self.actions.append(Action(AI.Action.LEAVE))
            return self.actions.popleft()

        if (self.colDim * self.rowDim) - len(self.uncovered) == self.totalMines - len(self.mines):
            #print("ALL TILES ARE MINES, FLAGGING ALL AND LEAVING\n")
            for i in range(self.colDim):
                for j in range(self.rowDim):
                    if self.board[i][j] == -2:
                        self.actions.append(Action(AI.Action.FLAG, i, j))
            self.actions.append(Action(AI.Action.LEAVE))
            return self.actions.popleft()

        while self.actions:
            neighbor = self.neighbors.popleft()
            self.uncovered.add((neighbor[0], neighbor[1]))
            self.board[neighbor[0]][neighbor[1]] = number
            return self.actions.popleft()

        if self.start:
            self.start = False
            self.uncovered.add((self.startX, self.startY))
            self.board[self.startX][self.startY] = number

            if number == 0:
                for i, j in self.get_neighbors(self.startX, self.startY):
                    self.actions.append(Action(AI.Action.UNCOVER, i, j))
                    self.neighbors.append((i, j))
            return self.actions.popleft()

        else:
            neighbor = self.neighbors.popleft()
            self.uncovered.add((neighbor[0], neighbor[1]))
            self.board[neighbor[0]][neighbor[1]] = number

            for i, j in self.uncovered:
                neighbors = self.get_neighbors(i, j)
                if self.board[i][j] == 0 and len(neighbors) != 0:
                    for t, k in neighbors:
                        if self.board[t][k] == -2:
                            self.actions.append(Action(AI.Action.UNCOVER, t, k))
                            self.neighbors.append((t, k))
                            return self.actions.popleft()

                if self.board[i][j] > 0 and len(neighbors) != 0:
                    covered_neighbors = []
                    flagged_neighbors = []
                    for t, k in self.get_all_neighbors(i, j):
                        if self.board[t][k] == -2:  # covered tile
                            covered_neighbors.append((t, k))
                        elif self.board[t][k] == -1:  # mine
                            flagged_neighbors.append((t, k))

                    if self.board[i][j] == len(flagged_neighbors):
                        for t, k in covered_neighbors:
                            self.actions.append(Action(AI.Action.UNCOVER, t, k))
                            self.neighbors.append((t, k))
                            return self.actions.popleft()

                    elif len(covered_neighbors) == self.board[i][j] - len(flagged_neighbors):
                        for t, k in covered_neighbors:
                            self.actions.append(Action(AI.Action.FLAG, t, k))
                            self.neighbors.append((t, k))
                            self.mines.add((t, k))
                            return self.actions.popleft()

            #print("Choosing Random Tile\n")
            min_chance = float('inf')
            min_chance_tile = None

            covered = [(i, j) for i in range(self.rowDim) for j in range(self.colDim) if self.board[i][j] == -2]

            for tile in covered:
                chance = self.calculate_chance(tile)
                if chance < min_chance:
                    min_chance = chance
                    min_chance_tile = tile
            self.actions.append(Action(AI.Action.UNCOVER, min_chance_tile[0], min_chance_tile[1]))
            self.neighbors.append((min_chance_tile[0], min_chance_tile[1]))
            return self.actions.popleft()

        return Action(AI.Action.LEAVE)

    def get_neighbors(self, x, y):
        neighbors = []
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= i < self.rowDim and 0 <= j < self.colDim and (x, y) != (i, j) and (i, j) not in self.uncovered:
                    neighbors.append((i, j))
        return neighbors

    def get_all_neighbors(self, x, y):
        neighbors = []
        for k in range(x - 1, x + 2):
            for t in range(y - 1, y + 2):
                if 0 <= k < self.rowDim and 0 <= t < self.colDim and (k, t) != (x, y):
                    neighbors.append((k, t))
        return neighbors

    def calculate_chance(self, tile):
        neighbors = self.get_all_neighbors(tile[0], tile[1])
        flagged_neighbors = sum(2 for neighbor in neighbors if neighbor in self.mines)
        uncovered_neighbors = sum(1 for neighbor in neighbors if neighbor in self.uncovered and neighbor not in self.mines)
        if not neighbors:
            return 100
        likelihood = flagged_neighbors + uncovered_neighbors
        return likelihood
