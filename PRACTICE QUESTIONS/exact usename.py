print("==================EXTRACT USERNAME FROM EMAIL===================")
email=input("ENTER EMAIL ADDRESS:")
username=""
for i in email:
    if i == "@":        
     break
    username=username + i
print("USERNAME:",username)

# WRITE A PROGRAM THAT WILL CONVERT CELSIUS VALUE TO FAHRENHEIT:-
cel_temp=int(input("ENTER TEMPERATURE IN CELSIUS ="))
fah_temp=(cel_temp)*1.8
convert=fah_temp+32
print("Fahrenheit Temperature is:",convert)
