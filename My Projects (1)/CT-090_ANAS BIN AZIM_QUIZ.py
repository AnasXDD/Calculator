N = int(input("Enter your number :"))

for i in range(N):
    for j in range(N):
        if (i == j) or ((N - j -1) == i):
            print("*", end = "  ")
        else:
            print(" ", end = "  ")
    print("")