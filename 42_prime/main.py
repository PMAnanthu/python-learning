"""Prime number check"""

def check_prime(number,index):
    """
    Check the given number is prime number 
    """
    if number==index:
        return True
    else:
        if number % index == 0:
            return False
        else:
            return check_prime(number=number,index=index+1)
  
def check(number):
    """
    Check given number is prime or not
    """
    return check_prime(number=number,index=2)

val=int(input("Number : "))
if val==1 or check(val):
    print("Prime Number")
else:
    print("Not a prime number")   
