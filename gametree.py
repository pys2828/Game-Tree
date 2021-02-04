# Here is the board class; it has two attributes, knight and pawns; each piece is a pair of numbers between 0 and 7
class Board:
	def __init__(self, pieces):
		self.knight = pieces[0]
		self.pawns = pieces[1:]

	# prints board as 8 strings, 1 per line, with optional heading
	def printBoard(self, heading=""):
		if (heading):
			print(heading)
		board = [" - - - - - - - -"]*8
		(x,y) = self.knight
		row = board[x]
		board[x] = row[0:2*y+1] + "X" + row[2*y+2:]
		for (x,y) in self.pawns:
			row = board[x]
			board[x] = row[0:2*y+1] + "o" + row[2*y+2:]
		for row in board[:]:
			print(row)

	# returns list of knight moves that will eat a pawn, if any
	def findGoodMoves(self):
		(x0, y0) = self.knight
		moves = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
		goodMoves = []
		for (x, y) in moves:
			(x1, y1) = (x0 + x, y0 + y)
			#print ("trying move ", x, y)
			if (x1, y1) in self.pawns:
				goodMoves += [(x, y)]
		return goodMoves

	# returns a new board that's a copy of this one
	def copyBoard(self):
		newBoard = Board([self.knight]+self.pawns)
		return newBoard

	#given a board and a move, compute the next board
	def applyMove(self, move):
		(x0, y0) = self.knight
		(x, y) = move
		if ((x0 + x) >= 0 and (y0 + y) >= 0) and ((x0 + x) < 8 and (y0 + y) < 8):
			self.knight = (x0 + x, y0 + y)
			if self.knight in self.pawns:
				self.pawns.remove(self.knight)
			return True
		else:
			return False

	## Part 1
	def printGoodMovesBoard(self):
                original = self.copyBoard()
                new = self.copyBoard()
                for i in self.findGoodMoves():
                        new.applyMove(i)
                        a = (i[0] + self.knight[0], i[1] + self.knight[1])
                        new.printBoard("Board with move " + str(a))
                        new = original
                        
                        
		

	def printAllMovesBoard(self):
                moves = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
                for (x,y) in moves:
                        (xo, yo) = self.knight
                        last = (xo+x,yo+y)
                        if last[0] >= 0 and last[1] >= 0 and last[0] < 8 and last[1] < 8:
                                self.knight = last
                                if last in self.pawns:
                                        self.pawns.remove(self.knight)
                                        print("")
                                        self.printBoard("Board with move " + str(last))
                                        self.pawns.append(last)
                                        self.knight = (xo, yo)
                                else:
                                        print("")
                                        self.printBoard("Board with move " + str(last))
                                        self.knight = (xo,yo)
                        else:
                                print("")
                                print("Invalid move: " + str(last))
                        

## Part 2
def dfsCapture(board):
        zion = False
        pos = board.findGoodMoves()
        if len(pos) == 1 and len(board.pawns) == 1:
                return True
        elif len(pos) == 0:
                return False
        else:
                for i in pos:
                        new = board.copyBoard()
                        new.applyMove(i)
                        zion = dfsCapture(new) or zion
        return zion
                

def bfsCapture(board):
        movelist = []
        def helperfunc(board):
                pos = board.findGoodMoves()
                for i in pos:
                        new = board.copyBoard()
                        new.applyMove(i)
                        helperfunc(new)
                movelist.append((len(pos), len(board.pawns),))
        helperfunc(board)
        return (1,1) in movelist

## Part 3
def findPath(board):
        def helperpath(board, pospath = [board.knight]):
                pos = board.findGoodMoves()
                if len(pos) >= 1:
                        new = board.copyBoard()
                        new.applyMove(pos[0])
                        pospath.append(new.knight)
                        return helperpath(new, pospath)
                else:
                        return pospath
        if dfsCapture(board):
                return helperpath(board)
        return []
                                
                        


## Part 4
def findAllPaths(board, path=None, totpath = None):
        if path == None:
                path = []
        if path == []:
                path.append(board.knight)
        if totpath == None:
                totpath = []
        pos = board.findGoodMoves()
        moves = pos
        for i in moves:
                new = board.copyBoard()
                new.applyMove(i)
                good = new.findGoodMoves()
                if len(good) == 0 and len(new.pawns) == 0:
                        newpath = path + [new.knight]
                        totpath.append(newpath)
                newpath = path[:] + [new.knight]
                findAllPaths(new, newpath, totpath)
        return totpath
                        
                        
                
                





