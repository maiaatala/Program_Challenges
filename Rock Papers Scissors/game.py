import random

choices = ["rock", "paper", "scissors"]
user_wins, computer_wins = 0, 0

while True:
    user_loop_choice = input("Choose Rock, Paper, Scissors or type Q to quit\nUser: ").lower()
    
    if user_loop_choice == "q":
        print()
        break
    if user_loop_choice in choices:
        pc_loop_choice = random.choice(choices)
        print("PC:", pc_loop_choice.capitalize()+"!")
        if user_loop_choice == pc_loop_choice:
            print(">>> It's a tie!")
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
        print("Opção inválida!")
    print()

print("┌────────────────────────────┐")
print("|       Pc Won overall!      |") if computer_wins > user_wins else print("|      User Won overall!     |")
print(f"|  Score:  PC: %2i  User: %2i  |" % (computer_wins, user_wins))
print("└────────────────────────────┘")
