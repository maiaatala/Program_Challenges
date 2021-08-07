import random
# https://www.reddit.com/r/dailyprogrammer/comments/n94io8/20210510_challenge_389_easy_the_monty_hall_problem/

# create an object for the players
class player():
    name = choice1 = choice2 = None
    wins = 0
    
    def __init__(self, *args):
        self.name, self.choice1, self.choice2 = args

def monty_hall(choice1, choice2): # return 1 for win and 0 for loss
    doors = [1, 2, 3]  # all the available doors
    right_door = random.randrange(1,4)  # randomly choses the right door
    
    if choice1 == 'r':
        choice1 = random.choice(doors)
    #block works out which door the showman will open
    monty_chosen_door = doors.copy()  # string with the possible doors the showman can open
    monty_chosen_door.remove(choice1)  # the showman won't ever open the choice in step2
    if right_door in monty_chosen_door: # if the right door is one of the options, it will remove that
        monty_chosen_door.remove(right_door)
    else:
        monty_chosen_door.remove(random.choice(monty_chosen_door))
    # works out which door are available for step4
    doors.remove(monty_chosen_door[0])  #the only door left in monty_chosen_door is the door the showman opens, therefore, the doors left for stage 4 are all but that one.
    
    # bocks controls the manipulation of choice2
    if choice2 == 'stay':
        choice2 = choice1
    elif choice2 == 'switch':
        doors.remove(choice1)
        choice2 = doors[0]
    elif choice2 == 'r':
        choice2 = random.choice(doors)
    elif choice2 not in doors:
        choice2 = choice1
        
    #see if the person won or not
    if choice2 == right_door:
        return(1)
    else:
        return(0)

random.seed()  # start the random
# print("Monyty hall problem, 3 doors, choosing #1 and not switching: %s" % ('win' if monty_hall(1, False) == 1 else 'lost') )
nrounds = 1000
alice = player('Alice', 1, 'stay')
bob = player('Bob', 1, 'switch')
carol = player('Carol', 'r', 'r')
dave = player('Dave', 'r', 'stay')
erin = player('Erin', 'r', 'switch')
frank = player('Frank', 1, 2)
gina = player('Gina', 1, 'stay')
players = [alice, bob, carol, dave, erin, frank, gina]

for i in players:
    for j in range(nrounds):
        temp = (monty_hall(i.choice1, i.choice2))
        i.wins += temp
        if i.name == 'Gina' and temp == 0:
            i.choice2 = 'stay' if i.choice2 == 'switch' else 'switch'
    print("%5s win rate: %.2f" % (i.name, ((i.wins/nrounds)*100)))
