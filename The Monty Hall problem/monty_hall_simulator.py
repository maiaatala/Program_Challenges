import random
# https://www.reddit.com/r/dailyprogrammer/comments/n94io8/20210510_challenge_389_easy_the_monty_hall_problem/
# Alice chooses door #1 in step 2, and always sticks with door #1 in step 4.
# Bob chooses door #1 in step 2, and always switches to the other closed door in step 4.

# create an object for the players
class player():
    name = choice1 = choice2 = None
    wins = 0
    
    def __init__(self, *args):
        self.name, self.choice1, self.choice2 = args

#create an funcion based on their choices

def monty_hall(choice1, choice2):
    win = None
    doors = [1, 2, 3]  # all the available doors
    right_door = random.randrange(1,4)  # randomly choses the right door
    doors.remove(choice1)   # removes the 1st chosen door (won't intefere with the code)
    # removes one of the other doors
    if doors[0] == right_door:
        doors.remove(doors[1])
    elif doors[1] == right_door:
        doors.remove(doors[0])
    else:  # removes a random door
        doors.remove(doors[random.randrange(0,2)])
    #if the person switches doors, than this block will switch their choice
    if choice2 == 'switch':
        choice1 = doors[0]
    #if the person ahs a favorite door, than this block will pick it
    if choice1 == right_door:
        win = 1
    else:
        win = 0
    return(win)
    # print(right_door)

random.seed()  # start the random
# print("Monyty hall problem, 3 doors, choosing #1 and not switching: %s" % ('win' if monty_hall(1, False) == 1 else 'lost') )
nrounds = 1000
rounds = [""]
Alice = player('Alice', 1, 'stay')
Bob = player('Bob', 1, 'Switch')
players = [Alice, Bob]

for i in players:
    for j in range(nrounds):
        i.wins += (monty_hall(i.choice1, i.choice2))
    print("%s win rate: %.2f" % (i.name, ((i.wins/nrounds)*100)))
    rounds.clear()
