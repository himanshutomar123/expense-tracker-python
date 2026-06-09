print("PRINT ALL THE UNIQUE COMBINATION OF 1,2,3 AND 4.")
num= [1,2,3,4]
for i in num: #outer loop i=1,1
    for j in num:#inner loop j=1,2
        if i != j:
            print(i,j)