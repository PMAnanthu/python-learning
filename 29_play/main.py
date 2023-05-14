"""Simple play code"""

ROW1 = ["😀","😄","🤣"]
ROW2 = ["😍","😉","😘"]
ROW3 = ["😔","😕","🤨"]
MAP = [ROW1,ROW2,ROW3]
print(f"{ROW1}\n{ROW2}\n{ROW3}\n")
position = input("Where do you want to put treasure? ")
column = int(position[0])
row = int(position[1])
MAP[row-1][column-1]="🎁"
print(f"{ROW1}\n{ROW2}\n{ROW3}\n")
