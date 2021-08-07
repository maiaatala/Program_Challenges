import random
# https://www.reddit.com/r/dailyprogrammer/comments/n94io8/20210510_challenge_389_easy_the_monty_hall_problem/
# Alice chooses door #1 in step 2, and always sticks with door #1 in step 4.
# Bob chooses door #1 in step 2, and always switches to the other closed door in step 4.

def monty_hall(choice, switch, favorite_door = 2):
    win = None
    doors = [1, 2, 3]  # all the available doors
    right_door = random.randrange(1,4)  # randomly choses the right door
    doors.remove(choice)   # removes the 1st chosen door (won't intefere with the code)
    # removes one of the other doors
    if doors[0] == right_door:
        doors.remove(doors[1])
    elif doors[1] == right_door:
        doors.remove(doors[0])
    else:  # removes a random door
        doors.remove(doors[random.randrange(0,2)])
    #if the person switches doors, than this block will switch their choice
    if switch:
        choice = doors[0]
    #if the person ahs a favorite door, than this block will pick it
    if favorite_door != None:
        if doors[0] == favorite_door:
            choice = doors[0]
    if choice == right_door:
        win = 1
    else:
        win = 0
    return(win)
    # print(right_door)

random.seed()  # start the random
# print("Monyty hall problem, 3 doors, choosing #1 and not switching: %s" % ('win' if monty_hall(1, False) == 1 else 'lost') )
nrounds = 1000
rounds = [""]
players = [
    {
        'nome' : 'Alice',
        'choice1' : 1,
        'switch' : False,
        'favorite' : None
    },
    {
        'nome' : 'Bob',
        'choice1' : 1,
        'switch' : True,
        'favorite' : None
    }
]
for i in range(len(players)):
    for j in range(nrounds):
        rounds.append(monty_hall(players[i]['choice1'], players[i]['switch'], players[i]['favorite']))
    players[i]['winrate'] = (rounds.count(1)/nrounds)*100
    print("%s win rate: %.2f" % (players[i]['nome'], players[i]['winrate']))
    rounds.clear()
