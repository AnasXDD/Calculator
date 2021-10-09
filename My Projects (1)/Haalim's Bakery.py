
print('Welcome to HAALIM BAKERS')
print("We offer the following items: ")
print("\t1.Bownie(Rs 50/-,serves 1)")
print("\t2.Cream Roll(Rs 30/-,serves 1)")
print("\t3.Muffins(Rs 40/-,serves 1)")
print("\t4.Exit")
summ=0

while True:
    x=int(input("Enter your choice number"))
    if x==1:
        a=int(input("Enter how many brownies do you want: "))
        summ+=(50*a)
    elif x==2:
        b=int(input("Enter how many Cream Rolls do you want: "))
        summ+=(30*b)
    elif x==3:
        c=int(input("Enter how many Muffins do you want: "))
        summ+=(40*c)
    elif x==4:
        break
print("Your total bill is Rs.",summ)
print("Your order will be delivered in 30 minutes\nThank you for coming!!!")