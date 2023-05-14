"""Pizz Bill Calculator"""


if __name__=="__main__":
    size=input("Enter pizza size: S, M or L? ")
    pepperoni = input("Do you want pepperoni: Y or N? ")
    cheese = input("Do you want extra cheese: Y or N? ")
    BILL = 0
    if size in ("S", "s"):
        BILL =15
        if pepperoni in ("Y", "y"):
            BILL += 2
    elif size in ("M", "m"):
        BILL = 20
        if pepperoni in ("Y", "y"):
            BILL += 3
    else:
        BILL = 25
        if pepperoni in ("Y", "y"):
            BILL += 3
    if cheese in ("Y", "y"):
        BILL += 1
    print(f"Total price of pizza is {BILL}")
