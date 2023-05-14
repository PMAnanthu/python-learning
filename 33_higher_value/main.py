"""Max function code"""

student_scores = input("Enter student scores ").split(" ")

HIGHEST = 0
for score in student_scores:
    if int(score) > HIGHEST:
        HIGHEST = int(score)
print(f"Highest score is {HIGHEST}")
