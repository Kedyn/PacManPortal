from maze import Maze
from astar import mazeToGridMap

maze = Maze('assets/maze.txt', None)

grid = mazeToGridMap(maze.rows)

print(grid)


'''
from game import Game

game = Game()

game.play()
'''
