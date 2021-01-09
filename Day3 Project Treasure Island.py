print('''
*******************************************************************************************
          |               |                |                 |                  |          
 _________|____________.=""_;=.____________|_________________|__________________|__________
|             |    ,-"_,=""     `"=.|               |                  |                   
|_____________|____"=._O`"-._        `"=.___________|__________________|___________________
          |            `"=._O`"=._      _`"=._               |                  |          
 _________|_________________:=._O "=._."_.-="'"=.____________|__________________|__________
|             |      __.--" , ; `"=._O." ,-"""-._ ".                   |                   
|_____________|___._"  ,. .` ` `` ,  `"-._"-._   ". !__________________|___________________
          |       |O`"=._` , "` `; .". ,  "-._"-._; ;        |                  |          
 _________|_______| ;`-.O`"=._; ." ` '`."\` . "-._ /_________|__________________|__________
|             |   |O;    `"-.O`"=._``  '` " ,__.--O;|                  |                   
|_____________|___| ;     (#) `-.O `"=.`_.--"_O.-; ;|__________________|___________________
____/______/______|O;._    "      `".O|O_.--"    ;O;_____/______/______/______/______/_____
/______/______/____"=._O--._        ; | ;        ; ;_/______/______/______/______/______/__
____/______/______/_____"=._O--._   ;O|O;     _._;O;_____/______/______/______/______/_____
/______/______/______/______/"=._O._; | ;_.--"O.--"__/______/______/______/______/______/__
____/______/______/______/______/_"=.O|O_.--""____/______/______/______/______/______/_____
/______/______/______/______/______/_________/______/______/______/______/______/_______/__
*******************************************************************************************
''')
print()
print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
side = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\" \n").lower()
if side =="left":
    action = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across. \n").lower()
    if action == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if door == "red":
            print("You found yourself in a room full of fire and burn... GAME OVER!!!")
        elif door == "Blue" or "blue":
            print("You found a beat in the room and the beast eats you... GAME OVER!!!")
        elif door == "Yellow" or "yellow":
            print("You just found the treasure opened and waiting for someone to grab it and you are the lucky one... YOU WIN!!!!!")
        else:
            print("You have choosen a room that doesn't exist... GAME OVER!!!)
    elif action == "Swim" or action == "swim":
        print("You tried to swim and got eaten by the shark who has spotted you... GAME OVER!!!")
else:
    print("You just got hit by a truck and died... GAME OVER!!!")

