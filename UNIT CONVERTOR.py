# --------------------------------------------------------------- UNIT CONVERTOR -----------------------------------------------------------------
print("================UNIT CONVERTOR===============")
print("================MENU==================")
while True:
    print("\n Choose Conversion Type")
    print("1.Kilometers to Miles")
    print("2.Miles To Kilometers")
    print("3.Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Kilograms to Pounds")
    print("6. Pounds to Kilograms")
    print("7. Exit")

    choice = int(input("ENTER YOUR CHOICE:"))
    if choice == 1:
        km=float(input("ENTER KILOMETERS:"))
        miles=km * 0.621371
        print(f"{km}km={miles:.2f}miles")

    elif choice == 2:
        miles=float(input("ENTER MILES:"))
        km = miles/0.621371
        print(f"{miles:.2f}miles ={km}km")

    elif choice == 4:
        fahrenheit=float(input('ENTER TEMPERATURE IN fahrenheit:0'))
        celsius=(fahrenheit-32)*5/9
        print(f"{fahrenheit}°F = {celsius:.2f}°C")
    
    elif choice == "3":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit:.2f}°F")

    elif choice == "5":
        kg = float(input("Enter kilograms: "))
        pounds = kg * 2.20462
        print(f"{kg} kg = {pounds:.2f} pounds")

    
    elif choice == "6":
        pounds = float(input("Enter pounds: "))
        kg = pounds / 2.20462
        print(f"{pounds} pounds = {kg:.2f} kg")

    # Exit
    elif choice == "7":
        print("Thanks for using Unit Converter!")
        break

    else:
        print("Invalid choice! Please try again.")

    
        
    

    


