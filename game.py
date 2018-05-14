#   @@@@@@@@@@@@@@@@@@@@@@
#   @@@@@@@@@@@@@@@@@@@@@@
#   
# @@Author
#       Akshit Gattani
#       Amish Khandelwal
#   
#   @@@@@@@@@@@@@@@@@@@@@@
#   @@@@@@@@@@@@@@@@@@@@@@


import os
import sys

ciD = iD = 1
cjD = jD = 1
char = "A"

# function to describe the game
def gameDescription():
    # calls file with game description
    #os.system("head -11 gameDesc.txt")
    descHandler = open("gameDesc.txt", "r")
    desclist = descHandler.readlines()
    for i in desclist:
        print(i.rstrip('\n'), end="\n")

# function to display map
def mapDisplay():
    global iD, jD, char, ciD, cjD
    # checks if coordinates are greater than zero and less than 4
    if ciD > 0 and cjD > 0 and ciD < 4 and cjD < 4:
        iD = ciD
        jD = cjD
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        noToList = {0: ["A", "B", "C"], 1: ["D", "E", "F"], 2: ["G", "H", "I"]}
        try:
            iD = noToList[iD-1]
            jD = iD[jD-1]
        except (KeyError, IndexError):
            print("You hit a wall! \nChoose a valid direction")
            coordinateCorrection()
            nextRoomDirection()
        for i in grid:
            for j in i:
                if (i == iD) and (j == jD):
                    print("*", end="")
                    char = j
                print(j, end="\t")

            print()
        dispOptions()
    else:
        print("You hit a wall! \n Choose a valid direction")
        coordinateCorrection()
        nextRoomDirection()

# function to display options with numeric inputs to choose
def dispOptions():
    # calls file with options
    #os.system("head -5 displayOptions.txt")
    descHandler = open("displayOptions.txt", "r")
    desclist = descHandler.readlines()
    for i in desclist:
        print(i.rstrip('\n'), end="\n")


# funtion to display clue depending on character of the room
def clueDisplay():
    global char
    clueHandler = open("clues.txt", "r")
    charToNumber = {'A': 1, 'B': 2, 'C': 3, 'D': 4,
                    'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9}
    clueList = clueHandler.readlines()
    num = charToNumber[char]
    print(clueList[num - 1].rstrip('\n'))

    exClueHandle = open("exClue.txt", "r")
    exClueList = exClueHandle.readlines()
    if char == 'C':
        print(exClueList[0])
    if char == 'E':
        print(exClueList[1])
    if char == 'F':
        print(exClueList[2])
    if char == 'I':
        print(exClueList[3])
    if char == 'G':
        print(exClueList[4])

    dispOptions()
    
	

# function to handle user answer
def answerVictim():
    name = "Albert(Butler), Bruce(Husband), Cercei(PA), Dickens(Accountant), Eugene(lover), Freddy(son), Gerard(Hotel Security), Hermoinee(waitress), Issac(Boyfriend)"
    namelist = name.split(",")
    for i in namelist:
        print(i)
    print("Whom do you think is the Murderer? (Type full name)")
    
    answer = input(": ")
    answer = answer.lower()
    if answer == "issac":
        print("You guessed it RIGHT!!")
        print("\n\nWhy did he kill Clair?\nIssac had grudge against Eugene because Eugene did wrong with Hermoinie. He wanted to make Eugene Suffer.\nHe found that Eugene was in need of money and was using Clair to get it, so he decided to kill Eugene. So he used his key to open the room, which only hotel management have, but being a rookie at using fire-arm, he missed his shot and only grazed Eugene, killing Claire in the process.")
        print()
        sys.exit(0)
    else:
        print("You guessed it WRONG!!")
        print("TRY AGAIN")
        dispOptions()
    
    # os.system("timeout 30")

# function to move the user
def nextRoomDirection():
    direction = input("Which Direction: ")
    global ciD, cjD
    #checking the input direction and changing user's coordinate value accordingly
    if direction == "a" or direction == "A":
        cjD -= 1
    if direction == "d" or direction == "D":
        cjD += 1
    if direction == "w" or direction == "W":
        ciD -= 1
    if direction == "s" or direction == "S":
        ciD += 1

    # os.system("cls")
    os.system("clear")
    mapDisplay()

# function to handle user input
def userInput(inputChoice):
    if inputChoice == 1:
        answerVictim()
    if inputChoice == 2:
        clueDisplay()
    if inputChoice == 3:
        nextRoomDirection()

# correcting bad user input
def coordinateCorrection():
    global ciD, cjD
    if cjD <= 0:
        cjD += 1
    if cjD > 3:
        cjD -= 1
    if ciD <= 0:
        ciD += 1
    if ciD > 3:
        ciD -= 1

# driver function
def main():
    gameDescription()
    mapDisplay()

    try:
        inputChoice = int(input("Your Choice: "))
    except (TypeError, ValueError):
        print("invalid input.")
        inputChoice = 0
    
    while (True):
        userInput(inputChoice)
        try:
            inputChoice = int(input("Your Choice: "))
        except (TypeError, ValueError):
           print("invalid input.")
           inputChoice = 0 

main()
