"""Stone Scissors Paper Game"""
import random

ITEMS=["🪨","🔪","📄"]
print("Welecome To Rock Scissors Paper")
print("================================")
COMPUTER_SCORE = 0
USER_SCORE = 0
USER_CHOICE_STR="start"
while USER_CHOICE_STR != "e":
    USER_CHOICE_STR = input("Enter your choice 0-Rock 1-Scissors 2-Paper e-exit :\t")
    if USER_CHOICE_STR != "e" and USER_CHOICE_STR.isdigit():
        USER_CHOICE = int(USER_CHOICE_STR)
        if USER_CHOICE in (0,1,2):
            COMPUTER_CHOICE = random.randint(0,2)
            print(f"Your choice is {ITEMS[USER_CHOICE]}")
            print(f"Computer choice is {ITEMS[COMPUTER_CHOICE]}")
            if USER_CHOICE==0:
                if COMPUTER_CHOICE == 0:
                    print("DRAW 💥")
                elif COMPUTER_CHOICE == 1:
                    print("You Wone 😊")
                    USER_SCORE += 1
                elif COMPUTER_CHOICE == 2:
                    print("Computer Wone 😒")
                    COMPUTER_SCORE += 1
            if USER_CHOICE==1:
                if COMPUTER_CHOICE == 0:
                    print("Computer Wone 😒")
                    COMPUTER_SCORE += 1
                elif COMPUTER_CHOICE == 1:
                    print("DRAW 💥")
                elif COMPUTER_CHOICE == 2:
                    print("You Wone 😊")
                    USER_SCORE += 1
            if USER_CHOICE==2:
                if COMPUTER_CHOICE == 0:
                    print("You Wone 😊")
                    USER_SCORE += 1
                elif COMPUTER_CHOICE == 1:
                    print("Computer Wone 😒")
                    COMPUTER_SCORE += 1
                elif COMPUTER_CHOICE == 2:
                    print("DRAW 💥")
            print(f"Total Score Computer: {COMPUTER_SCORE}  Your: {USER_SCORE}")
print("GAME OVER!!!")
