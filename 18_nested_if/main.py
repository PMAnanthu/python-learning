"""Nested IF code"""

if __name__=="__main__":
    hight = float(input("Enter your hight in cm? "))
    if hight >= 120:
        age = int(input("Enter your age? "))
        if age <= 12:
            print("Engoy ride after pay 5$")
        elif age <= 18:
            print("Engoy ride after pay 7$")
        else:
            print("Engoy ride after pay 12$")
             
    else:
        print("Sorry better luck next time :( ")
        
    