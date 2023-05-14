"""Stone Scissors Paper Game"""
import random

ITEMS=["🪨","🔪","📄"]
print("Welecome To Stone Scissors Paper")
print("================================")
COMPUTER_SCORE = 0
USER_SCORE = 0
USER_CHOICE="start"
while USER_CHOICE != "e":
    user_choice_str = input("Enter your choice 1-stone 2-scissors 3-paper e-exit :\t")
    if user_choice_str != "e":
        USER_CHOICE = int(user_choice_str)
        COMPUTER_CHOICE = random.randint(1,3)
        print(f"Your choice is {ITEMS[USER_CHOICE-1]}")
        print(f"Computer choice is {ITEMS[COMPUTER_CHOICE-1]}")
        if USER_CHOICE==1:
            if COMPUTER_CHOICE == 1:
                print("DRAW 💥")
            elif COMPUTER_CHOICE == 2:
                print("You Wone 😊")
                USER_SCORE += 1
            elif COMPUTER_CHOICE == 3:
                print("Computer Wone 😒")
                COMPUTER_SCORE += 1
        if USER_CHOICE==2:
            if COMPUTER_CHOICE == 1:
                print("Computer Wone 😒")
                COMPUTER_SCORE += 1
            elif COMPUTER_CHOICE == 2:
                print("DRAW 💥")
            elif COMPUTER_CHOICE == 3:
                print("You Wone 😊")
                USER_SCORE += 1
        if USER_CHOICE==3:
            if COMPUTER_CHOICE == 1:
                print("You Wone 😊")
                USER_SCORE += 1
            elif COMPUTER_CHOICE == 2:
                print("Computer Wone 😒")
                COMPUTER_SCORE += 1
            elif COMPUTER_CHOICE == 3:
                print("DRAW 💥")
        print(f"Total Score Computer: {COMPUTER_SCORE}  Your: {USER_SCORE}")
print("GAME OVER!!!")
