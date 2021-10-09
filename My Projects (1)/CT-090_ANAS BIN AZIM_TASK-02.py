# ANAS BIN AZIM      CT-090      TASK 02

list=[]

for i in range(int(input("Enter lenght of tuple : "))):
    count = ""
    a = input("Enter Number : ")
    for i in a:
        if i>="0" and i<="9":
            count=count+i
    list.append(int(count))

tple=tuple(list)
print(tple)