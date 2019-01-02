from tkinter import Tk, ttk
from random import randint
from time import sleep

""" Current issues/to do:
- deal with a draw
- when someone wins it doesn't show the last move before closing
"""

# Empty game board
class Board(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # 3x3 grid of square object (def below)
        squares = [[Square(self) for i in range(3)] for i in range(3)]
        for i in range(3):
            for j in range(3):
                # Commented out code is for labelling buttons when debugging
                #squares[j][i].configure(text="r={},c={}".format(i,j))
                squares[j][i].grid(row=i, column=j)
        self.squares = squares

# Squares that make up game board
class Square(ttk.Button):
    def __init__(self, master, text=""):
        super().__init__(master, text="")
        self.master = master
        self.configure(command=self.user_chooses_square)
    
    # For printing button when debugging
    def __repr__(self):
        return "Button: {}".format(self.cget("text"))   
    
    # For printing button when debugging
    def __str__(self):
        return "Button: {}".format(self.cget("text"))
    
    # Action when clicked
    def user_chooses_square(self):
        if self.cget("text") == "":
            self.configure(text=user_shape)
            global next_turn
            next_turn = "computer"
            check_for_winner()

    def computer_chooses_square(self):
        self.configure(text=computer_shape)

def computer_plays():
    # Randomly chooses square until an empty one is found
    i, j = randint(0, 2), randint(0, 2)
    while board.squares[j][i].cget("text"):
    	i, j = randint(0, 2), randint(0, 2)
    board.squares[j][i].computer_chooses_square()
    
    global next_turn 
    next_turn = "user"
    check_for_winner()
    # TO DO: make this do better than choosing randomly

def check_for_winner():
	# Makes a list of all rows/cols/diagonals
    list_of_rows = [[board.squares[i][j] for i in range(3)] for j in range(3)]
    list_of_columns = [[board.squares[j][i] for i in range(3)] for j in range(3)]
    list_of_diagonals = [[board.squares[i][i] for i in range(3)], [board.squares[i][2-i] for i in range(3)]]
    list_of_triples = list_of_rows + list_of_columns + list_of_diagonals

    # Checks for three in a row 
    for triple in list_of_triples:
    	if triple[0].cget("text") == triple[1].cget("text") and triple[0].cget("text") == triple[2].cget("text") and triple[0].cget("text") != "":
    		if triple[0].cget("text") == user_shape:
    			print("You win!")
    			return new_game()
    		else:
    			print("You lose...")
    			return new_game()
    if next_turn == "computer":
    	computer_plays()
        
def new_game():
	# TO DO: choice whether to play new game or quit
	sleep(2)
	print("New game...")
	global board
	board.destroy()
	board = Board(root)
	board.pack()
	global next_turn
	next_turn = "user"

user_shape = "X"
computer_shape = "O"
# TO DO: user chooses this

# Set up and title the main window
root = Tk()
root.title("TicTacToe")

# Set up new board
board = Board(root)
board.pack()
next_turn = "user"

# Run tkinter event loop
root.mainloop()