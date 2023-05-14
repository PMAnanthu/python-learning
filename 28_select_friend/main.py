import random

if __name__=="__main__":
    namestr = input("Enter name seperated by comma: ")
    names = namestr.split(",")
    random_number = random.randint(0, len(names)- 1)
    print(f"{names[random_number]}")