"""Average code"""
student_hights = input("Enter student hights ").split()

LEN = 0
SUM =0
for hight in student_hights:
    SUM += int(hight)
    LEN += 1

print(f"Average {round(SUM/LEN)}")
