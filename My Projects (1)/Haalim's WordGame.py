a=['A','E','I','M','Q','U','Y']
b=['B','F','J','N','R','V','Z']
c=['C','G','K','O','S','W']
d=['D','H','L','P','T','X']

print("Col#1\t\tCol#2\t\tCol#3\t\tCol#4")
for i in range(len(c)):
    print(a[i]+ "\t\t" +b[i]+"\t\t" +c[i]+ "\t\t" +d[i])
print("Y\t\tZ")

x=int(input("\nHow many letters does your word contains? "))

s=[]
for i in range(1,x+1):
    print("In which column , the letter",i,"of your word exist?",end=" ")
    m=int(input())
    if m==1:
        s.append(a)
    elif m==2:
       s.append(b)
    elif m==3:
        s.append(c)
    elif m==4:
        s.append(d)

for i in range(len(s)):
    for j in s[i]:
        print(j,end="\t\t")
    print()

word=""
print("\nOk, so now for one last time,tell that\n")
for i in range(1,x+1):
    print("In which column,the letter",i,"of your word exist")
    n=int(input())
    word+=str(s[i-1][n-1])

print("The word you have guessed is",word)