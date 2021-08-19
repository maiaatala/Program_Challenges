import random

choices = ["rock", "paper", "scissors"]
user_wins, computer_wins, rounds = 0, 0, 1

print(" --Rock Paper Scissors Game-- ")
print("  ¶ Made by: Ana C. M. Atala\n")

while True:
    print("# Round %2i # " % rounds)
    user_loop_choice = input("Choose Rock, Paper, Scissors or type Q to quit\nUser: ").lower()
    
    if user_loop_choice == "q":
        print()
        break
    if user_loop_choice in choices:
        rounds += 1
        pc_loop_choice = random.choice(choices)
        print("PC:", pc_loop_choice.capitalize()+"!")
        if user_loop_choice == pc_loop_choice:
            print(">>> It's a tie!")
            computer_wins += 1
            user_wins += 1
        elif user_loop_choice == 'rock':
            if pc_loop_choice == 'paper':
                print(">>> PC Win!")
                computer_wins += 1
            else:
                print(">>> User Win!")
                user_wins += 1
        elif user_loop_choice == 'paper':
            if pc_loop_choice == 'scissors':
                print(">>> PC Win!")
                computer_wins += 1
            else:
                print(">>> User Win!")
                user_wins += 1
        else:
            if pc_loop_choice == 'rock':
                print(">>> PC Win!")
                computer_wins += 1
            else:
                print(">>> User Win!")
    else:
        print("Invalid Input")
    print()

print("┌────────────────────────────┐")
print("|      Rounds Played: %2i     |" % (rounds-1))
print("|       Pc Won overall!      |") if computer_wins > user_wins else print("|      User Won overall!     |")
print(f"|  Score:  PC: %2i  User: %2i  |" % (computer_wins, user_wins))
print("└────────────────────────────┘")
print("\nbyeee.")