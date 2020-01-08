from array import *
from math import *
class GridObject:
	isObstacle = False
	isPath = False
	fScore = 0
	def __init__(self, row, col):
		self.r = row
		self.c = col
def createGrid(size):
	grid = []
	i = 0
	for r in range(0,size):
		row = []
		for c in range(0,size):
			g = GridObject(r,c)
			row.insert(c, g)
		grid.insert(r, row)
	return grid
def drawGrid(grid):
	for r in grid:
		for i in r:
			if not i.isPath and not i.isObstacle:
				print("*", end=" ")
			if i.isPath and not i.isObstacle:
				print("#", end=" ")
			if i.isObstacle:
				print("X", end=" ")
		print("\n")
def heuristic_distance(start, goal):
	return pow(sqrt(pow(goal.r-start.r,2)+pow(goal.c-start.c,2)),2)
def findNeighbors(n):
	neighbors = []
	if not grid[n.r-1][n.c-1].isObstacle:
		neighbors.append(grid[n.r-1][n.c-1]) 
	if not grid[n.r-1][n.c].isObstacle:
		neighbors.append(grid[n.r-1][n.c])
	if not grid[n.r-1][n.c+1].isObstacle:
		neighbors.append(grid[n.r-1][n.c+1]) 
	if not grid[n.r][n.c-1].isObstacle:
		neighbors.append(grid[n.r][n.c-1])
	if not grid[n.r][n.c+1].isObstacle:
		neighbors.append(grid[n.r][n.c+1]) 
	if not grid[n.r+1][n.c-1].isObstacle:
		neighbors.append(grid[n.r+1][n.c-1]) 
	if not grid[n.r+1][n.c].isObstacle:
		neighbors.append(grid[n.r+1][n.c])
	if not grid[n.r+1][n.c+1].isObstacle:
		neighbors.append(grid[n.r+1][n.c+1]) 
	return neighbors
def makePath(cameFrom, start):
	path = []
	for x in cameFrom:
		path.append(x)
	path.insert(0,start)
	return path
def findPath(start, goal, h):
	#https://en.wikipedia.org/wiki/A*_search_algorithm
	#I used distance^2 as my h
	openSet = []
	openSet.append(start)
	cameFrom = {
	}
	gScore = {
		start: 0 
	}
	fScore = {
		start: inf
	}
	current = start
	while len(openSet) != 0:
		if current == goal:
			return makePath(cameFrom,start)
		for i in openSet:
			if i.r == current.r and i.c == current.c:
				print("Current:", current.r, current.c, " -- Removing")
				openSet.remove(i)
		if current not in gScore:
			gScore[current] = heuristic_distance(start, current)
		neighbors = findNeighbors(current)
		fs = []
		for neighbor in neighbors:
			d = heuristic_distance(neighbor, goal)
			neighbor.fScore = gScore[current] + d
			fs.append(neighbor.fScore)
			if neighbor not in openSet:
				openSet.append(neighbor)
		chosen = min(fs)
		for z in neighbors:
			if z.fScore == chosen:
				cameFrom[z] = current
				gScore[z] = z.fScore
				fScore[z] = gScore.get(z, inf) + heuristic_distance(z,goal)
				current = z
	return []
if __name__ == "__main__":
	grid = createGrid(15)
	#Cannot find path around 4 wide obstacle due to the way findNeighbors works
	for r in range(6,9):
		for c in range(5,8):
			grid[r][c].isObstacle = True
	path = findPath(grid[1][4],grid[13][6],heuristic_distance(grid[1][4],grid[13][6]))
	for x in path:
		for r in grid:
			for i in r:
				if x.r == i.r and x.c == i.c: 
					i.isPath = True
	drawGrid(grid)