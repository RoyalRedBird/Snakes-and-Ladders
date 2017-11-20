print ("Welcome to Snakes and Ladders!")

print ("Keep in mind that there are snakes on spaces 17, 62, 64, 54, 87, 93, 95 and 98.")

print ("Don't worry, there are ladders on spaces 1,4,9, 21, 28, 51, 72 and 80.")

print ("Copy and Paste http://tinyurl.com/yd9k3s2s into your browser to see the board I used for reference.")

import random

player = 0

rolls_taken = 0

snakes_hit = 0

ladders_hit = 0

while player < 100:

    Player_Roll = input("To roll the dice, please hit enter.")

    if Player_Roll == (""):

        rolls_taken = rolls_taken + 1

        Dice_Number = random.uniform(1,12)

        Dice_Number = int(Dice_Number)

        print ("You rolled a %s." % Dice_Number)

        player = player + Dice_Number

        print ("You are currently on space %s." % player)

    else:

        print ("Just hit enter, nothing more.")

    if player == 17:

        player = 7

        snakes_hit = snakes_hit + 1

        print ("Oh noes, you hit a snake! You have moved down to space %s!" % player)

    if player == 54:

        player = 34

        snakes_hit = snakes_hit + 1

        print ("Oh noes, you hit a snake! You have moved down to space %s!" % player)

    if player == 62:

        player = 19

        snakes_hit = snakes_hit + 1

        print ("Oh noes, you hit a snake! You have moved down to space %s!" % player)

    if player == 64:

        player = 60

        snakes_hit = snakes_hit + 1

        print ("Oh noes, you hit a snake! You have moved down to space %s!" % player)

    if player == 87:

        player = 36

        snakes_hit = snakes_hit + 1

        print ("Oh noes, you hit a snake! You have moved down to space %s!" % player)

    if player == 93:

        player = 73

        snakes_hit = snakes_hit + 1

        print ("Oh noes, you hit a snake! You have moved down to space %s!" % player)

    if player == 95:

        player = 75

        snakes_hit = snakes_hit + 1

        print ("Oh noes, you hit a snake! You have moved down to space %s!" % player)

    if player == 98:

        player = 79

        snakes_hit = snakes_hit + 1

        print ("Oh noes, you hit a snake! You have moved down to space %s!" % player)

    if player == 1:

        player = 38

        print ("Congrats, you hit a ladder! You have moved up to space %s!" % player)

    if player == 4:

        player = 14

        ladders_hit = ladders_hit + 1

        print ("Congrats, you hit a ladder! You have moved up to space %s!" % player)

    if player == 9:

        player = 31

        ladders_hit = ladders_hit + 1

        print ("Congrats, you hit a ladder! You have moved up to space %s!" % player)

    if player == 21:

        player = 42

        ladders_hit = ladders_hit + 1

        print ("Congrats, you hit a ladder! You have moved up to space %s!" % player)

    if player == 28:

        player = 84

        ladders_hit = ladders_hit + 1

        print ("Congrats, you hit a ladder! You have moved up to space %s!" % player)

    if player == 51:

        player = 67

        ladders_hit = ladders_hit + 1

        print ("Congrats, you hit a ladder! You have moved up to space %s!" % player)

    if player == 72:

        player = 91

        ladders_hit = ladders_hit + 1

        print ("Congrats, you hit a ladder! You have moved up to space %s!" % player)

    if player == 80:

        player = 99

        ladders_hit = ladders_hit + 1

        print ("Congrats, you hit a ladder! You have moved up to space %s!" % player)

print ("Congrats on making it to space 100!")

print ("You have rolled the dice %s times." % rolls_taken)

print ("You have landed on %s snake(s)." % snakes_hit)

print ("You have landed on %s ladder(s)." % ladders_hit)
