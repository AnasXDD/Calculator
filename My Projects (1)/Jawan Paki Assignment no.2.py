eng = 80
islamiat = 75
maths = 95
totalmarks = 300
obtainmarks = eng + islamiat + maths
per = (obtainmarks / totalmarks)*100
print(per)
if (per > 80):
    print ("A1-Grade")
elif (per < 80 and per > 70):
    print("A-Grade")
elif (per < 70 and per > 60):
    print("B-Grade")
else :
    print ("Fail")
