"""BMI V.2"""


if __name__=="__main__":
    weight = float(input("Weight in KG : "))
    hight = float(input("Hight in m: "))
    bmi = round(weight / (hight ** 2))
    print("BMI: "+str(int(bmi)))
    if bmi < 18.5:
        print("Under weight!")
    elif bmi < 25:
        print("Normal")
    elif bmi < 30:
        print("Over Weight")
    elif bmi <35:
        print("obese")
    else:
        print("clinically obese")
    