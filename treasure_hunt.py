print('''
888                                                          
888                                                          
888                                                          
888888888d888 .d88b.  8888b. .d8888b 888  888888d888 .d88b.  
888   888P"  d8P  Y8b    "88b88K     888  888888P"  d8P  Y8b 
888   888    88888888.d888888"Y8888b.888  888888    88888888 
Y88b. 888    Y8b.    888  888     X88Y88b 888888    Y8b.     
 "Y888888     "Y8888 "Y888888 88888P' "Y88888888     "Y8888  
                                                             
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************\n\n''')


print("welcome to treasure island")
print("your target is to find the treasure")
choice1 = input('You\'are at crossroad where you want to go? Type "left" or "right".\n').lower()

if choice1 == "left":
    #continue the game.
    choice2 = input('You\'ve come to a sea, there is an island in middle of the sea. Type "wait" to wait for the boat or Type "swim" to swim across the sea.\n').lower()
    if choice2 == "wait":
        #Game will continue
        choice3 = input("You arrive at island unharmed, There is a house with 3 doors. one red one yellow and one blue. Which color do you choose?\n").lower()
        if choice3 == "red":
            print("Its a room full of fire, Game Over")
        elif choice3 == "yellow":
            print("************You found the treasure you win!************")
        elif choice3 == "blue":
            print("you enter a room of dragons. Game Over")
        else:
            print("You choose a door that doesn't exist, Game Over")
    else:
        print("You get attacked by an angry shark. Game Over")
else:
    print("Game Over, you fell into a lake")