                                                # RENT CALCULATOR(MINI PROJECT)
rent=int(input("Enter Your Rent:"))
food=int(input("Enter Your Food Price:"))
electricity_spend=int(input("Enter The Total Electricity_Spend:"))
charge_per_unit=int(input('Enter Charge per unit:'))
persons=int(input("Enter How Many Person Is Living:"))

Total_bill= electricity_spend*charge_per_unit
print("Electricity:",Total_bill)
output=(rent+food+Total_bill) /persons
print("Each Person Will Pay:",output)