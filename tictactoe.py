#******************************************************************************
# tictactoe.py
#******************************************************************************
# Name: Ron Balaban
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
# None
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#
import random

class TTTBoard:
   
    def __init__(self):
        self._board=[[" "," "," "],[" "," "," "],[" "," "," "]]
        # This is our board in the beginning, empty for now.
        
    def display(self):
        for row in self._board:
            for entry in row:
                print("{0:3}".format(entry),end="")
            print("")
        # The nested for loop prints the board nicely, if called upon.
              
    def set(self,row,entry,choice):
        self._board[row][entry]= choice
        # This tells the board what we want it to look like, where we choose to put an x or o.
        
    def occupied(self,row,entry):
        if self._board[row][entry] == "x" or self._board[row][entry] == "o":
            return True
        if self._board[row][entry] == " ":
            return False
        # This if statement checks if myGame.occupied(0,2)- (1st row, 3rd entry) is occupied or not with an x or o.
        
    def _row_full(self,row,choice):
        if self._board[row][0]==choice and self._board[row][1]==choice and self._board[row][2]==choice:
            return True
        else:
            return False
        # This if statement checks if the entire row is all x or all o.
                                                                                            
    def _col_full(self,column,choice):
        if self._board[0][column]==choice and self._board[1][column]==choice and self._board[2][column]==choice:
            return True
        else:
            return False
        # This if statement checks if the entire column is all x or all o.
        
    def _diag_full(self,choice):
        if self._board[0][0]==choice and self._board[1][1]==choice and self._board[2][2]==choice:
            return True
        elif self._board[0][2]==choice and self._board[1][1]==choice and self._board[2][0]==choice:
            return True
        else:
            return False
        # This block checks if we have a \ or / diagonal in our board.

    def win_for(self,choice): 
        if self._row_full(0,choice) or self._row_full(1,choice) or self._row_full(2,choice):
            return True
        elif self._col_full(0,choice) or self._col_full(1,choice) or self._col_full(2,choice):
            return True
        elif self._diag_full(choice):
            return True
        else:
            return False
        # This checks if there is 3-in-a-row for x or o on the board, whichever the user chooses.
            
    def random_move(self,choice):
        unocc_list=[]
        if self._board[0][0]== " ":
            unocc_list.append([0,0])
        if self._board[0][1]== " ":
            unocc_list.append([0,1]) 
        if self._board[0][2]== " ":
            unocc_list.append([0,2])
        if self._board[1][0]== " ":
            unocc_list.append([1,0])
        if self._board[1][1]== " ":
            unocc_list.append([1,1])  
        if self._board[1][2]== " ":
            unocc_list.append([1,2])
        if self._board[2][0]== " ":
            unocc_list.append([2,0])
        if self._board[2][1]== " ":
            unocc_list.append([2,1])
        if self._board[2][2]== " ":
            unocc_list.append([2,2])  
        z= random.choice(unocc_list)
        self._board[z[0]][z[1]] = choice
        # This looks at the board and finds all empty spaces, and chooses a random one to be x or o, whichever we decide.
        
def main():
    ############################################################################
    # TEST CODE: DO NOT REMOVE IN FINAL SUBMISSION!
    ############################################################################
    myGame = TTTBoard()
    myGame.display()

    # Only run the following lines after you've written .set()
    # This should print something that looks kind of like
    # x o x
    # o x
    # x
    myGame.set(0, 0, "x")
    myGame.set(0, 1, "o")
    myGame.set(0, 2, "x")
    myGame.set(1, 0, "o")
    myGame.set(1, 1, "x")
    myGame.set(2, 0, "x")
    myGame.display()

    # Only run the following lines after you've written .occupied()
    # This should print out
    # True True True
    # True True False
    # True False False
    print(myGame.occupied(0,0),myGame.occupied(0,1),myGame.occupied(0,2))
    print(myGame.occupied(1,0),myGame.occupied(1,1),myGame.occupied(1,2))
    print(myGame.occupied(2,0),myGame.occupied(2,1),myGame.occupied(2,2))
        
    # Only run the following lines after you've written .win_for()
    # This should print out:
    # True
    # False
    print(myGame.win_for("x"))
    print(myGame.win_for("o"))

    # Only run the following lines after you've written .random_move()
    myGame.random_move("x")
    myGame.display()
    myGame.random_move("o")
    myGame.display()


    ############################################################################
    # END OF TEST CODE.
    # PLACE YOUR SIMULATION CODE BELOW.
    ############################################################################
    
myGame = TTTBoard()    
x_wins=0
o_wins=0
for game in range(10000):
    myGame=TTTBoard()
    for move in range(9):
        if move%2 ==0:
            myGame.random_move("x")
            if myGame.win_for("x"):
                x_wins+=1    
                break
        if move%2 ==1:     
            myGame.random_move("o")
            if myGame.win_for("o"):
                o_wins+=1
                break

print("x won {0} games.".format(x_wins))
print("o won {0} games.".format(o_wins))
print("There were {0} ties.".format(10000-x_wins-o_wins))
    

main()



