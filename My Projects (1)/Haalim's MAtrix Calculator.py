def matrix(r,c):
    matrix=[]
    for i in range(1,r+1):
        a=[]
        for j in range(1,c+1):
            print("Enter the element of row", i ,"column", j ,"of the matrix: ",end="")
            k=int(input())
            a.append(k)
        matrix.append(a)
    print("\nThe matrix is:\n")
    for i in range(r):
        for j in range(c):
            print(matrix[i][j],end="    ")
        print()
    return matrix


def addition(A,B):
    for i in range(len(A)):
        for j in range(len(A[0])):
                G=A[i][j]+B[i][j]
                print(G,end="    ")
        print()
    print()

def subtraction(A,B):
     for i in range(len(A)):
        for j in range(len(A[0])):
                G=A[i][j]-B[i][j]
                print(G,end="    ")
        print()
     print()

def multiplication(A,B):
    for i in range(len(A)):
        for j in range(len(B[0])):
            G=0
            for k in range(len(B)):
                G+=((A[i][j])*(B[i][j]))
            print(G,end="   ")
        print()

def transpose(A):
    for i in range(c):
        for j in range(r):
            G=A[j][i]
            print(G,end="   ")
        print()
    print()

print("HAALIM'S MATRIX CALCULATOR")

while True:
    print("\nWhich operation do you want to perform?")
    print("1. Addition of two matrices")
    print("2. Subtraction of two matrices ")
    print("3. Multiplication of two matrices")
    print("4. Transpose of a matrix")
    print("5. Exit\n")

    x=int(input())

    if x==1:
        print("ADDITION OF MATRICES\n")
        r=int(input("Enter number of rows of the matrices: "))
        c=int(input("Enter number of columns of matrices: "))

        print("\nEnter Matrix A: ")
        A=matrix(r,c)

        print("\nEnter Matrix B: ")
        B=matrix(r,c)
        
        print("\nBy adding the given matrices,we get:")
        addition(A,B)

    elif x==2:
        print("SUBTRACTION OF MATRICES\n")
        r=int(input("Enter number of rows of the matrices: "))
        c=int(input("Enter number of columns of matrices: "))

        print("\nEnter Matrix A: ")
        A=matrix(r,c)

        print("\nEnter Matrix B: ")
        B=matrix(r,c)

        print("\nBy subtracting the given matrices,we get:")
        subtraction(A,B)

    elif  x==3:
        print("MULTIPLICATION OF MATRICES\n")
        r=int(input("Enter number of rows of Matrix A: "))
        c=int(input("Enter number of columns of Matrix A: "))

        print("\nEnter Matrix A: ")
        A=matrix(r,c)

        r2=int(input("\nEnter number of rows of Matrix B: "))
        c2=int(input("Enter number of columns of Matrix B: "))

        if c==r2:
            print("\nEnter Matrix B: ")
            B=matrix(r2,c2)

            print("\nBy muktiplying the two matrices,we get:\n")
            multiplication(A,B)

        else:
            print("\nMatrix multiplication can only be done if the number of columns of first matrix is equal to number of rows of second matrix\n")

    elif x==4:
        print("TRANSPOSE OF MATRIX\n")
        r=int(input("Enter number of rows of the matrixA: "))
        c=int(input("Enter number of columns of matrixB: "))

        print("\nEnter the Matrix:\n")
        A=matrix(r,c)

        print("\nThe transpose of the given matrix is:\n")
        transpose(A)

    elif x==5:
        break
    
    f=input("Do you want to run the program again(y/n)\n")
    if f != 'y':
        break
