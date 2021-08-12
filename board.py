import random
class Board:

    def __init__(self, size: int):
        row = 0
        this_board = []
        self.queens = 0
        self.queenCoordinates = []
        while row < size:
            new_row = []
            column = 0
            while column<size:
                #new_row.append(f"[{column},{row}]")
                if (random.randint(0,7)==0):
                    new_row.append("[Q]")
                    self.queens += 1
                else:
                    new_row.append(f"[_]")
                column += 1
            this_board.append(new_row)
            row += 1
        self.board = this_board

    def render(self):
        for row in self.board:
            for square in row:
                print(square,end="")
            print("")
        print(f"This board has {self.queens} Queens.")

    def getQueenCoordinates(self):
        x = 0
        y = 0
        size = len(self.board)
        while y < size:
            x = 0
            while x < size:
                square = self.board[y][x]
                if self.board[y][x][1]=="Q":
                    self.queenCoordinates.append([x,y])
                x+=1
            y+=1
        print("Queens are located at: "+str(self.queenCoordinates))

    def checkQueenCaptures(self):




