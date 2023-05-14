if __name__=="__main__":
    hight = float(input("Enter your hight in cm? "))
    bill = 0
    if hight >= 120:
        age = int(input("Enter your age? "))
        if age <= 12:
            bill =5
        elif age <= 18:
            bill =7
        else:
            bill =12
        photo = input("do you want phot y-yes n-no: ")
        if photo == "y":
            bill += 3
        print(f"Enjoy your ride, total bill is {bill}")
            
    else:
        print("Sorry better luck next time :( ")
    
        
    