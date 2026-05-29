num=input("ENTER SOMETHING HERE:")
def float_check(num):
    try:
        float(num)
        return True
    except:
        return False

print(float_check(num))    

text = input('ENTER STRING HERE:')
def string_check(text):
    try:
        str(text)
        return True
        
    except:
        return False
print(string_check(text))