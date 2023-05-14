if __name__=="__main__":
    year = int(input("Year: "))
    if year % 4 == 0:
        if year % 100==0:
            if year %400 == 0:
                print("Leap Year")
            else:
                print("Not a leap year")
        else:
            print("Leap Year")
    else:
        print("Not a leap year")
    
        
    