def power(x,y):
    if(y==1):
        return(x)
    if(y!=1):
        return(x*power(x,y-1))
x=int(input("Enter base: "))
y=int(input("Enter exponential value: "))
print("Result:",power(x,y))