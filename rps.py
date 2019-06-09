from random import randint

yourScore = 0
compScore = 0

while True:

    #take input from player
    player = input('rock(r), paper(p), or scissors(s)?')
    chosen = randint(1,3)

    #assign letters to random numbers
    if chosen == 1:
        computer = "r"

    elif chosen == 2:
        computer = "p"

    else:
        computer = "s"

    print("Player: " + player + " vs Computer: " + computer)

    #determine and print results
    if player == computer:
        print("Draw!!!")
    elif player == "r" and computer == "s":
        print("You Win!")
        yourScore +=1
    elif player == "p" and computer == "r":
        print("You Win!")
        yourScore +=1
    elif player == "s" and computer == "p":
        print("You Win!")
        yourScore +=1
    else:
        print("You Lose!")
        compScore +=1

    print("Player: " + str(yourScore) + ", Computer: " + str(compScore))
    print("______________________________")
