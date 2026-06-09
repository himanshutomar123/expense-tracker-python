text = input("ENTER WORD: ")
char = input("ENTER CHAR: ")

for i in range(len(text)):
    if text[i] == char:
        print("POSITION NUMBER OF CHAR:", i)

        