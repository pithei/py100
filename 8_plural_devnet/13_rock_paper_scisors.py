"""
Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), 
compare them, print out a message of congratulations to the winner, 
and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock

Concepts for this week:

While loops
Infinite loops
Break statements
"""

while True:
    player1_input = input("Player 1 please chooser rock/paper/scissors: ")
    player2_input = input("Player 2 please chooser rock/paper/scissors: ")
    if ( player1_input == player2_input ):
        print("Congratulations, draw!")
    elif ( player1_input == "paper" and player2_input == "rock" ) :
        print("Congratulations, Player 1, you have won!")
    elif ( player1_input == "rock" and player2_input == "scissors" ) :
        print("Congratulations, Player 1, you have won!")
    elif ( player1_input == "scissors" and player2_input == "paper" ) :
        print("Congratulations, Player 1, you have won!")
    else:
        print("Congratulations, Player 2, you have won!")
    new_game = input("Do you want to start new game? y/n: ")
    if ( new_game == "n" ):
        print("Ending the game, have a nice day!")
        break

"""
Sample solutions, https://www.practicepython.org/solution/2014/04/02/08-rock-paper-scissors-solutions.html

import sys

user1 = input("What's your name?")
user2 = input("And your name?")
user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(compare(user1_answer, user2_answer))


---------------------------------------------
print('''Please pick one:
            rock
            scissors
            paper''')

while True:
    game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
    player_a = str(input("Player a: "))
    player_b = str(input("Player b: "))
    a = game_dict.get(player_a)
    b = game_dict.get(player_b)
    dif = a - b

    if dif in [-1, 2]:
        print('player a wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif dif in [-2, 1]:
        print('player b wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    else:
        print('Draw.Please continue.')
        print('')
"""