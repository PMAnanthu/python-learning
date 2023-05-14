"""BMI Calculator"""

if __name__=="__main__":
    weight = float(input("Weight in KG : "))
    hight = float(input("Hight in m: "))
    bmi = weight / (hight ** 2)
    print("BMI: "+str(int(bmi)))
        
    