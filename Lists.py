'''
check version history for what changed

eight ball was good

deck shuffle went out of range due to checking a random number index from 0 to 51 on a suit list which was only 4 long.

I adjusted your sieve to work.  Couple minor changes.  you mostly had the solution.

I added some code that might send you in the right direction on
tic tac toe.  Resubmit for credit if you choose.




'''

#LISTS (35PTS TOTAL)
#In these exercises you write functions. Of course, you should not only write the functions,
#you should also write code to test them. For practice, you should also comment your
#functions as explained above.
import random

#PROBLEM 1 (8-ball - 5pts)
# A magic 8-ball, when asked a question, provides a random answer from a list.
# The code below contains a list of possible answers. Create a magic 8-ball program that
# prints a random answer.


def eight_ball():
    print(input("Ask the magic eight ball any yes or no question and it will give an answer!"))
    answer_list = ["It is certain!", "It is decidedly so!", "Without a \
    doubt!", "Yes, definitely!", "You may rely on it!", "As I see it,\
    yes.", "Most likely.", "Outlook good.", "Yes!", "Signs point to yes.",
    "Reply hazy, try again.", "Ask again later...", "Better not tell you \
    now...", "Cannot predict now...", "Concentrate and ask again!", "Don't count on it!",\
    "My reply is no.", "My sources say no.", "Outlook not so good...",\
    "Very doubtful."]
    choice = random.randrange(0,20) #we will use this to pick a random string from answer_list
    choice = int(choice)
    print(answer_list[choice])

eight_ball()



print("")
# PROBLEM 2 (Shuffle - 5pts)
# A playing card consists of a suit (Heart, Diamond, Club, Spade) and a value (2,3,4,5,6,7,8,9,10,J,Q,K,A).
# Create a list of all possible playing cards, which is a deck.
# Then create a function that shuffles the deck, producing a random order.
import random
def shuffle_deck():
    suit_list = ["Hearts", "Diamonds", "Clubs", "Spades"]
    card_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    card_deck = []
    shuffled_deck = []
    for suit in suit_list:
        for card in card_list: # nested loops allow for the lists to be combined
            card_deck.append([card, suit])
    print(card_deck)
    for i in range(len(card_deck)): # this will make 52 cards because the number of types of cards times the number of suits is 52
        card = card_deck.pop(random.randrange(len(card_deck)))
        #number = random.randrange(len(card_list))
        #deck = print(card_list[cards], "of", suit_list[number])
        print(card)
        shuffled_deck.append(card)
    print(shuffled_deck)
shuffle_deck()



print("")
# PROBLEM 3 (The sieve of Eratosthenes - 10pts)
# The sieve of Eratosthenes is a method to find all prime numbers between
# 1 and a given number using a list. This works as follows: Fill the list with the sequence of
# numbers from 1 to the highest number. Set the value of 1 to zero, as 1 is not prime.
# Now loop over the list. Find the next number on the list that is not zero,
# which, at the start, is the number 2. Now set all multiples of this number to zero.
# Then find the next number on the list that is not zero, which is 3.
# Set all multiples of this number to zero. Then the next number, which is 5
# (because 4 has already been set to zero), and do the same thing again.
# Process all the numbers of the list in this way. When you have finished,
# the only numbers left on the list are primes.
# Use this method to determine all the primes between 1 and 1000.

number_list = []
prime_numlist = []

for i in range(1002):
    number_list.append(i)
print(number_list)

for number in number_list:
    if number != 0 and number >= 2:
        for i in range(number, len(number_list)):
            #number_list = str(number_list)
            if number_list[i]%number == 0 and number_list[i] != number:
                number_list[i] = 0

print(number_list)


print("")
# PROBLEM 4 (Tic-Tac-Toe - 15pts)
# Write a Tic-Tac-Toe program that allows two peo1ple to play the game against each other.
# In turn, ask each player which row and column they want to play.
# Make sure that the program checks if that row/column combination is empty.
# When a player has won, end the game.
# When the whole board is full and there is no winner, announce a draw.
# This is a fairly long program to write (60 lines or so).
# It will definitely help to use some functions.
# I recommend that you create a function display_board() that gets the board
# as parameter and displays it,
# a function get_row_column() that asks for a row or a column (depending on a parameter)
# and checks whether the user entered a legal value,
# and a function winner() that gets the board as argument and checks if there is a winner.
# Keep track of who the current player is using a global variable player that you can
# pass to a function as an argument if the function needs it.
# I also use a function opponent(), that takes the player as argument and returns
# the opponent. I use that to switch players after each move.

# The main program will be something along the lines of (in pseudo-code):
# display board
# while True:
#   ask for row
#   ask for column
#       if row/column already occupied:
#           display error
#   place player marker in row/col
#   display board
#   check for winner:
#       announce winner
#       break
#   check board full:
#       announce draw
#       break
#   switch player

#FUNCTIONS
'''
def player_input():
    player = (input("Enter and X or an O and the computer will take the opposite symbol: ")).upper()
    print(player)

def check_rowcolumn():
    pass
    #x = input(int("Enter an x position to see if that spot is open: "))
    #y = input(int("Enter a y position to see if that spot is open: "))
    # if x is not available print error
    # if y is not available print error
'''
def display(length): # display board
    for i in range(int(length)):
        print(" " * length , " | " , " " * length , " | ", " " * length)
        print(" " * length , "-----" * length , " " * length)
    print(" " * length, " | ", " " * length, " | ", " " * length)
    print()

def position_andprint(board,player): #takes player's position
    #board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    xposition = int(input("Enter a row, 1, 2, or 3: "))
    yposition = int(input("Enter a column, 1, 2, or 3: "))
    #print(board[xposition])
    #print(board[yposition])
    board[yposition][xposition] = player
    #if xposition = full, error


def check_win(board, player):
    '''
    win_combinations = ((1, 2, 3) , (4, 5, 6), (7, 8, 9), (1, 5, 9), (2, 5, 8), (3, 5, 7), (1, 4, 7), (3, 6, 9))
    for value in win_combinations:
        if board[value[0] - 1] == board[value[1] - 1] and board[value[1] - 1] == board[value[2] - 1]:
            return board[value[0] - 1]
    '''
    if board[0][0] == board[0][1] == board[0][2] == player:
        print(player, "WINS!")


def draw_board(board):
    #count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end = " ")
            #count += 1
        print()

'''
make list for the board [" ", " ", ]
USE LISTS

enter row, (1 2 or 3)
enter column (1,2 or 3)

create a bunch of functions and then make a while loop

row_count
col_count
check_win

create a "check if full function"

player == "X"
player == "O"


IN THE WHILE LOOP
row = int(input)
col = int input

for col in range(len(board)):
    col_count = 0

'''

done = False
#display(2)
player = "X"
board = [["-","-","-"],["-","-","-"],["-","-","-"]]
while not done:
    draw_board(board)
    position_andprint(board, player)

    check_win(board, player)
