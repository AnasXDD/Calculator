# f = open("employee.txt","w")
# employee_id = int(input("Enter employee id : "))
# employee_name = input("Enter employee id : ")
# employee_salary = int(input("Enter employee salary : "))
# employee_id = str(employee_id)
# employee_salary = str(employee_salary)
# f.write(employee_id + "\n" + employee_name + "\n" + employee_salary)
# f.close()
# f = open("employee.txt", "r")
# temp = f.read()
# print(temp)
# f.close()

# f = open("employee.txt","w")
# employee_id = int(input("Enter employee id : "))
# employee_name = input("Enter employee name : ")
# employee_salary = int(input("Enter employee salary : "))
# employee_id = str(employee_id)
# employee_salary = str(employee_salary)
# f.write(employee_id + "\n" + employee_name + "\n" + employee_salary)
# f.close()
# f = open("employee.txt", "r")
# temp = f.read()
# print(temp)
# f.close()

from msvcrt import getch
import sys

petition = "Computer please answer me"
len_petition = len(petition)
char_count = 0
dot_count = 0
ans = ""
print("Enter Petition : ", end="")
while char_count < len_petition:
    sys.stdout.flush()
    getchar = getch()
    sys.stdout.flush()
    getchar = getchar.decode()
    if ord(getchar) == 13:
        break
    elif ord(getchar) == 8:
        print("\b \b", end="")
        char_count = char_count - 2
    elif getchar != "." and (dot_count == 0 or dot_count > 1):
        print(getchar, end='')
        sys.stdout.flush()
    elif getchar == "." and (dot_count == 0 or dot_count == 1):
        print(petition[char_count], end='')
        sys.stdout.flush()
        dot_count = dot_count + 1
    elif dot_count == 1:
        print(petition[char_count], end='')
        sys.stdout.flush()
        ans = ans + getchar
    char_count = char_count + 1
print("\n\nEnter Question", end='')
sys.stdout.flush()
input("")
print("Answer", ans)