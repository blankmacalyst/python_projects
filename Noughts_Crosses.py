#Noughts and Crosses Game

#Grid
grid = [0, 1, 2, 3, 4, 5, 6, 7, 8]

#Welcome
print("Welcome to Noughts and Crosses Game")

#Player name inputs
p1_name = input("What is name of Player 1? Player 1 is 'x': ")
p2_name = input("What is name of Player 2? Player 2 is 'o': ")

#Draw Grid
def draw_grid():
    print("-------------")
    print('|', grid[0], '|', grid[1], '|', grid[2], '|')
    print("-------------")
    print('|', grid[3], '|', grid[4], '|', grid[5], '|')
    print("-------------")
    print('|', grid[6], '|', grid[7], '|', grid[8], '|')
    print("-------------")

#Move input for player 1 
def p1():
        try:
            p1_input = int(input(p1_name + " select a space on the grid by entering a \
number to place an 'x': "))
        except ValueError:
            print("Error: Please enter a number, not a letter or symbol")
            p1()
        else:
            if p1_input not in range(9):
                print("Error: Please select a number on the grid 0-8 to place an 'x'")
                p1()
            elif grid[p1_input] == "x" or grid[p1_input] == "o":
                print("Error: This spot has been taken.")
                p1()
            else:
                grid[p1_input] = "x"
                draw_grid()

#Move input for player 2
def p2():
        try:
            p2_input = int(input(p2_name + " select a space on the grid by entering a \
number to place an 'o': "))
        except ValueError:
            print("Error: Please enter a number, not a letter or symbol")
            p2()
        else:
            if p2_input not in range(9):
                print("Error: Please select a number on the grid 0-8 to place an 'o'") 
                p2()
            elif grid[p2_input] == "x" or grid[p2_input] == "o":
                print("Error: This spot has been taken.")
                p2()
            else:
                grid[p2_input] = "o"
                draw_grid()

#Check for three x in a row
def p1_check():
    if grid[0] == "x" and grid[1] == "x" and grid[2] == "x" or \
        grid[3] == "x" and grid[4] == "x" and grid[5] == "x" or \
        grid[6] == "x" and grid[7] == "x" and grid[8] == "x" or \
        grid[0] == "x" and grid[3] == "x" and grid[6] == "x" or \
        grid[1] == "x" and grid[4] == "x" and grid[7] == "x" or \
        grid[2] == "x" and grid[5] == "x" and grid[8] == "x" or \
        grid[6] == "x" and grid[4] == "x" and grid[2] == "x" or \
        grid[0] == "x" and grid[4] == "x" and grid[8] == "x":
            print(p1_name + " Wins!")
            return "End Game"

#Check for three o in a row  
def p2_check():
    if grid[0] == "o" and grid[1] == "o" and grid[2] == "o" or \
         grid[3] == "o" and grid[4] == "o" and grid[5] == "o" or \
         grid[6] == "o" and grid[7] == "o" and grid[8] == "o" or \
         grid[0] == "o" and grid[3] == "o" and grid[6] == "o" or \
         grid[1] == "o" and grid[4] == "o" and grid[7] == "o" or \
         grid[2] == "o" and grid[5] == "o" and grid[8] == "o" or \
         grid[6] == "o" and grid[4] == "o" and grid[2] == "o" or \
         grid[0] == "o" and grid[4] == "o" and grid[8] == "o":
            print(p2_name + " Wins!")
            return "End Game"

#Check for a tie
def tie_check():
    if grid.count("x") + grid.count("o") == len(grid):
        print("Game is a tie")
        return "End Game"

#Play the game
def play():
    draw_grid()
    while True:
        p1()
        if p1_check() == "End Game":
            break
        if tie_check() == "End Game":
            break
        p2()
        if p2_check() == "End Game":
            break
        if tie_check() == "End Game":
            break

play()