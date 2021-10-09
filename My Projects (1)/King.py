print("MARKSHEET COMPARISION OF TWO STUDENTS")
One = input("Enter name of First Student : ")
Two = input("Enter name of Second Student : ")
x = int(input("How many subjects are there ? "))
if x==5 :
    print("There are 5 subjects")
    print("1-Maths")
    print("2-Physics")
    print("3-Chemistry")
    print("4-Urdu")
    print("5-English")
else :
    print("You are entering the wrong number. Try again :)")
    quit()

Maths1 = int(input("Enter Maths marks of First Student : "))
Physics1 = int(input("Enter Physics marks of First Student : "))
Chemistry1 = int(input("Enter Chemistry marks of First Student : "))
Urdu1 = int(input("Enter Urdu marks of First Student : "))
English1 = int(input("Enter English marks of First Student : "))
Maths2 = int(input("Enter Maths marks of Second Student : "))
Physics2 = int(input("Enter Physics marks of Second Student : "))
Chemistry2 = int(input("Enter Chemistry marks of Second Student : "))
Urdu2 = int(input("Enter Urdu marks of Second Student : "))
English2 = int(input("Enter English marks of Second Student : "))
percent1 = int(Maths1 + Physics1 + Chemistry1 + Urdu1 + English1)/5
print("Percentage of", One, "=", percent1,"%")
percent2 = int(Maths2 + Physics2 + Chemistry2 + Urdu2 + English2)/5
print("Percentage of", Two, "=", percent2,"%")
if percent1>=percent2 :
    print(One, "Got First Position")
    print(Two, "Got Second Position")
else :
    print(Two, "Got First Position")
    print(One, "Got Second position")