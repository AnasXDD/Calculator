print("\t\tWORD GUESS GAME\n\t\t================\n")
print("This program will guess the word which you have thought.\nHOW TO PLAY: Follow Rules which AI will tell you!\n")
alphabets ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nl = 3
print("Coloumn # 1  Coloumn # 2  Coloumn # 3  Coloumn # 4")
for i in range(0,len(alphabets)):
    print("     ",end="")
    print(alphabets[i],end="       ")
    if i==nl:
        print()
        nl += 4
print()
col1,col2,col3,col4=[],[],[],[]
for a in range(0,26,4):
    col1.append(alphabets[a])
    col2.append(alphabets[a+1])
for b in range(2,26,4):
    col3.append(alphabets[b])
    col4.append(alphabets[b+1])
code = ""
while True:
    n = input("Enter Coloumn Number in which your letter is present (Type \"done\" when finished) : ")
    if n.lower() == "done":
            break 
    if n>="1" and n<="4":
        code+=n
    else:
        print("Invalid Input!\nEnter Only 1-4 as there are 4 coloums only!")
        continue
print("1  2  3  4  5  6  7")
#print()
for row in code:
    if row=="1":
        for x in col1:
            print(x,end="  ")
        print()    
    elif row=="2":
        for x in col2:
            print(x,end="  ")
        print()   
    elif row =="3":
        for x in col3:
            print(x,end="  ")
        print()   
    else :
        for x in col4:
            print(x,end="  ")
        print()
#count=1
word=""

for alp in code:
    n = int(input("Enter Coloumn No. in which your letter is present : "))
    if n>=1 and n<=7:
        if n==1:
            if alp=="1":
                word=word+col1[0]
            elif alp=="2":
                word=word+col2[0]
            elif alp=="3":
                word=word+col3[0]
            else:
                word=word+col4[0]
        if n==2:
            if alp=="1":
                word=word+col1[1]
            elif alp=="2":
                word=word+col2[1]
            elif alp=="3":
                word=word+col3[1]
            else:
                word=word+col4[1]
        if n==3:
            if alp=="1":
                word=word+col1[2]
            elif alp=="2":
                word=word+col2[2]
            elif alp=="3":
                word=word+col3[2]
            else:
                word=word+col4[2]
        if n==4:
            if alp=="1":
                word=word+col1[3]
            elif alp=="2":
                word=word+col2[3]
            elif alp=="3":
                word=word+col3[3]
            else:
                word=word+col4[3]
        if n==5:
            if alp=="1":
                word=word+col1[4]
            elif alp=="2":
                word=word+col2[4]
            elif alp=="3":
                word=word+col3[4]
            else:
                word=word+col4[4]
        if n==6:
            if alp=="1":
                word=word+col1[5]
            elif alp=="2":
                word=word+col2[5]
            elif alp=="3":
                word=word+col3[5]
            else:
                word=word+col4[5]
        if n==7:
            if alp=="1":
                word=word+col1[6]
            elif alp=="2":
                word=word+col2[6]
            elif alp=="3":
                word=word+col3[6]
            else:
                word=word+col4[6]
    else:
        print("Invalid Input!\nEnter Only 1-7 as there are 7 coloums in this table!")
        continue
            
print("\nYour Word is :",word,"!")       
            
input("Press Enter to exit..")






