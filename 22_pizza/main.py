if __name__=="__main__":
    size=input("Enter pizza size: S, M or L? ")
    pepperoni = input("Do you want pepperoni: Y or N? ")
    cheese = input("Do you want extra cheese: Y or N? ")
    bill = 0
    if size == "S" or size == "s":
        bill =15
        if pepperoni == "Y" or pepperoni == "y":
            bill += 2
    elif size =="M" or size =="m":
        bill = 20
        if pepperoni == "Y" or pepperoni == "y":
            bill += 3
    else:
        bill = 25
        if pepperoni == "Y" or pepperoni == "y":
            bill += 3
    if cheese == "Y" or cheese == "y":
        bill += 1
    print(f"Total price of pizza is {bill}")