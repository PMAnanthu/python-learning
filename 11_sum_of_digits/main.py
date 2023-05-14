if __name__=="__main__":
    number = int(input("Enter the number?"))
    sum = 0
    while number > 0 :
        value = number%10
        sum += value
        number=number//10
    print("sum of the digit is : "+str(sum))
        
    