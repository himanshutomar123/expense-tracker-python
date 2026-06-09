print("WRITE A PYTHON PROGRAM TO PRINT THE FIRST 25 ODD NUMBER")

count_odd = 0

for i in range(1,51):
    if i % 2 != 0:
        print(i)
        count_odd = count_odd + 1

        if count_odd == 25:
            break