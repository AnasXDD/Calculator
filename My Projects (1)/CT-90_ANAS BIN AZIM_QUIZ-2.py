 num = (input("Enter any number : "))
 a=0
 for i in num:
     a = a+int(i)
 print(a)

# num=int(input("Enter Number: "))
# if num%2==1:
#     for row in range(num):
#         for col in range(num):
#             if row==col or ((row+col)==num-1):
#                 print("*",end="")
#             else:
#                 print(" ",end="")
#         print("")