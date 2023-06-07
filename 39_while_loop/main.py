"""While loop"""

def print_number_lessthan(num):
    """
    Print all number less than given number
    """
    counter = 0
    while counter < num:
        print(counter)
        counter += 1

if __name__=="__main__":
    print_number_lessthan(5)
