import random
import time

player1 = 0
player2 = 0

rounds_to_play = 4

for round_number in range(1, rounds_to_play, 1):
    print("Round", round_number, "Start Now!")
    time.sleep(2)
    roll = input("Player 1, Ready? (y/n)")
    if roll == "y":
        while roll == 'y':
            print('Rolling the dice...')
            time.sleep(.5)

            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            dice3 = random.randint(1, 6)

            print("You rolled:")
            print(dice1, dice2, dice3)
            time.sleep(1)

            if dice1 == dice2 or dice1 == dice3 or dice2 == dice3:
                print("yay! a pair (1p)")
                player1 = player1 + 1
                print("Player 1:", player1)
            elif dice1 == dice2 == dice3:
                print("yay! 3 of a kind! (5p)")
                player1 = player1 + 5
                print("Player 1:", player1)
            else:
                print("Sorry, you missed!")

            roll = 0
    else:
        print("Wow")

    time.sleep(5)

    roll = input("Player 2, Ready? (y/n)")
    if roll == "y":
        while roll == 'y':
            print('Rolling the dice...')
            time.sleep(.5)

            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            dice3 = random.randint(1, 6)

            print("You rolled:")
            print(dice1, dice2, dice3)
            time.sleep(1)

            if dice1 == dice2 or dice1 == dice3 or dice2 == dice3:
                print("Well done! You rolled a pair (1p)")
                player2 = player2 + 1
                print("Player 2:", player2)
            elif dice1 == dice2 == dice3:
                print("WOW! You hit a three of a kind! (5p)")
                player2 = player2 + 5
                print("Player 2:", player1)
            else:
                print("Sorry, Play again!")

            roll = 0
    else:
        print("end game")

    time.sleep(3)

print("The winner is...")
time.sleep(3)
if player1 > player2:
    print("Player 1 is the winner!")
elif player2 > player1:
    print("Player 2 is the winner!")
else:
    print("Start a new game, Draw!")
