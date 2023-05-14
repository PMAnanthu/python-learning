"""Sum of digit Code"""

if __name__=="__main__":
    number = int(input("Enter the number?"))
    TOTAL = 0
    while number > 0 :
        value = number%10
        TOTAL += value
        number=number//10
    print("sum of the digit is : "+str(TOTAL))
