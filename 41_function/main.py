"""Function example"""

def greet():
    """
    Function without parameter
    """
    print("Hi,")
    print("hope doing good\n")

def greet_with_name(name):
    """
    Function with parameter
    """
    print(f"Hi {name},")
    print("hope doing good\n")

if __name__=="__main__":
    greet()
    greet_with_name(name="Ananthu")