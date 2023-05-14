"""Tip Calculator code"""

if __name__=="__main__":
    bill = float(input("Enter the bill? "))
    ppl = float(input("Number of ppl? "))
    tip = float(input("Tip percent? "))
    total = bill + (bill * (tip/100))
    each = total / ppl
    each = round(each,2)
    print(f"Share {each}")
        
    