from tkinter import Tk, ttk
from random import randint

# Empty game board
class Board(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # 3x3 grid of square object (def below)
        squares = [[Square(self) for i in range(3)] for i in range(3)]
        for i in range(3):
            for j in range(3):
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
            check_for_winner()
            computer_plays()

    def computer_chooses_square(self):
        self.configure(text=computer_shape)

def computer_plays():
    # randomly chooses square until an empty one is found
    i, j = randint(0, 2), randint(0, 2)
    while board.squares[j][i].cget("text") != "":
    	i, j = randint(0, 2), randint(0, 2)
    board.squares[j][i].computer_chooses_square()

    check_for_winner()  

def check_for_winner():
	pass

user_shape = "X"
computer_shape = "O"
# TO DO: user chooses this

# Set up and title the main window
root = Tk()
root.title("TicTacToe")
# Create a new board
board = Board(root)
board.pack()
# Run tkinter event loop
root.mainloop()