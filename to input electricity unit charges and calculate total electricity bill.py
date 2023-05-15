unit=int(input("enter electricity unit"))
if(unit<=50):
    bill=unit*0.5
elif(unit>=50 and unit<=150):
    bill=(unit-50)*0.75 + 50*0.5
elif(unit>=150 and unit<=250):
    bill=50*0.5 + (unit-150)*1.2 + (unit-100)*0.75
else:
    bill=50*0.5 + (unit-150)*1.2 + (unit-100)*0.75 + (unit-250)*1.50
bill = bill + bill*0.2
print("total amout payble ",bill)