from msvcrt import getch
import sys
petition= "Computer please answer me"
len_petition=len(petition)
char_count=0
dot_count=0
ans=''
print("Enter Petition : ",end="" )
while char_count<len_petition:
    sys.stdout.flush()
    getchar=getch()
    sys.stdout.flush()
    getchar=getchar.decode()
    if ord(getchar)==13:
        break
    elif getchar!="." and (dot_count==0 or dot_count>1):
        print(getchar,end='')
        sys.stdout.flush()
    elif getchar =='.' and (dot_count==0 or dot_count==1):
        print(petition[char_count],end='')
        sys.stdout.flush()
        dot_count=dot_count+1
    elif dot_count==1:
        print(petition[char_count],end='')
        sys.stdout.flush()
        ans=ans+getchar
    char_count=char_count+1
print("Enter Question",end='')
sys.stdout.flush()
input=("")
print("Answer", ans )