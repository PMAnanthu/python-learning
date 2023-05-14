"""Ride Bill Calculator"""

if __name__=="__main__":
    hight = float(input("Enter your hight in cm? "))
    BILL = 0
    if hight >= 120:
        age = int(input("Enter your age? "))
        if age <= 12:
            BILL =5
        elif age <= 18:
            BILL =7
        else:
            BILL =12
        photo = input("do you want phot y-yes n-no: ")
        if photo == "y":
            BILL += 3
        print(f"Enjoy your ride, total bill is {BILL} ")
    else:
        print("Sorry better luck next time :( ")
