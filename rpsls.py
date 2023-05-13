'''
Use this values and rules to set the game logic
Values: 
0 - rock
1 - Spock
2 - paper
3 - lizard
4 - scissors

Scissors cuts paper. 
Paper covers rock. 
Rock crushes lizard. 
Lizard poisons Spock. 
Spock smashes scissors. 
Scissors decapitates lizard. 
Lizard eats paper. 
Paper disproves Spock. 
Spock vaporizes rock. 
Rock crushes scissors.
'''

# Libraries and variables
import random
import os
os.system("cls")

# os.system("cls") #clean screen

#initial values for counters
player_victories = 0
comp_victories = 0
round_number = 1
options = ("rock", "paper", "scissors", "lizard", "spock")

# Starting messages
print("Welcome to Rock-paper-scissors-lizard-Spock")
os.system("pause") # next screen

# Game cycle
while (player_victories < 3) and (comp_victories < 3):
    # New round starting screen
    # os.system("cls") # clean screen
    
    # Prints score
    print(f"\nThe computer has {comp_victories} wins")
    print(f"You have {player_victories} wins \n")
    print('*'*10)
    print("Round", round_number)
    print('*'*10)
    
    # Player choice
    player_choice = input("What do you choose? ").lower()    
    os.system("cls") # clean screen
    
    # Verifies that player's inpuit is a valid choice
    if not player_choice in options:
        print("POR FAVOR ELIGE UNA OPCIÓN VÁLIDA! \n")
        os.system("pause") # next screen
        continue
    
    # convert choice to number using if/elif/else
    def choice_to_number(choice):
        if choice == "rock":
            player_number = 0
        elif choice == "spock":
            player_number = 1
        elif choice == "paper":
            player_number = 2
        elif choice == "lizard":
            player_number = 3
        elif choice == "scissors":
            player_number = 4
        else:
            print("Please enter a valid choice! \n")
            player_number = None
        # don't forget to return the result!
        return player_number

    def rpsls(player_choice):         
        global player_victories
        global comp_victories
        global round_number
        # convert player_choice to player_number
        player_number = choice_to_number(player_choice)
        
        # print out the message for the player's choice
        print(f'Player chooses {player_choice}')
        
        # compute random guess for comp_choice
        comp_choice = random.choice(options)
        
        # print out the message for computer's choice
        print(f'Computer chooses {comp_choice}')
        
        # convert comp_choice to comp_number
        comp_number = choice_to_number(comp_choice)
        
        # compute result for player_choice vs comp_choice using module five
        result = (player_number - comp_number) % 5
        # print(result)
        
        # use if/elif/else to determine winner, print winner message
        if result == 0:
            print('Player and computer tie!')
        elif result > 2:
            print('Computer wins!')
            comp_victories = comp_victories + 1
        else:
            print('Player wins!')
            player_victories = player_victories + 1
        # print a blank line to separate consecutive games
        print()
       
        # Updates round number
        round_number = round_number + 1
        
        # Returns the updated values of player_victories, comp_victories, and round_number
        return player_victories, comp_victories, round_number

# Stops the game when player or computer obtains 3 victories
    if comp_victories == 3:
        # os.system("cls") #clean screen
        print(f"Computer has obtained {comp_victories} victories \nYOU HAVE LOST! HAHAHA")
        break
    elif player_victories == 3:
        # os.system("cls") #clean screen
        print(f"CONGRATULATIONS!!! you have obtained {player_victories} victories \n¡You are smarter than you seem!")
        break
    
    # call the rpsls function to play the round
    rpsls(player_choice)