# n = 1
# while n<=10 :
#     print("Square of", n, "is", n*n)
#     n=n+1


# while True:
#     n = int(input("Enter any number : "))
#     for i in range(1,11):
#         print(n, "*", i, "=", n*i)
#         continue


# a = 0
# b = 1
# n = int(input("Enter a number at which a fibonacci series is upto : "))
# if n<=0 :
#     print("Not Possible")
# elif n==1 :
#     print(a)
# elif n>=2 :
#     print("{},{}".format(a,b), end="")
#     for i in range(2,n):
#         c = a+b
#         print(",{}".format(c), end="")
#         a = b
#         b = c


# n = int(input("Enter number of rows : "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()


# age = int(input("Enter person's age : "))
# if age<2:
#     print("The person is a baby")
# elif age>=2 and age<4:
#     print("The person is a toddler")
# elif age>=4 and age<13:
#     print("The person is a kid")
# elif age>=13 and age<20:
#     print("The person is a teenager")
# elif age>=20 and age<65:
#     print("The person is an adult")
# else:
#     print("The person is an elder")


# n = int(input("Enter a number : "))
# a,b = 0,1
# if n<=0:
#     print("Not possible")
# elif n==1:
#     print(a)
# elif n>=2:
#     print("{},{}".format(a,b), end="")
#     for i in range(2,n):
#         c = a+b
#         print(",{}".format(c), end="")
#         a=b
#         b=c


# for i in range(1,21):
#     if i==9 or i==13:
#         continue
#     print(i, end=" ")


# while True:
#     year = int(input("Enter a year to be checked : "))
#     if year%4==0 or year%100==0 or year%400==0 :
#         print("This is a Leap Year")
#     else :
#         print("This is not a Leap Year")
#     continue

def check_armstrong(n):
    sum = 0
    order = len(str(n))
    copy_n = n
    while (n<0):
        digit = n % 10
        sum += (digit) ** order
        n = n//10
    if (sum == copy_n) :
        print(copy_n, " is an Armstrong Number ")
    else:
        print(copy_n, " is not an Armstrong number ")
y=check_armstrong(input("Enter any number"))
print(y)

