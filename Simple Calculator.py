while True:
    print(" A basic Calculator")
    print("Operators allowed are (+), (-), (*), (/) and (^)")
    a = float(input("select first number: "))
    op = input("select operator: ")
    b = float(input("select second number: "))
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a / b)
    elif op == "^":
        print(a ** b)
    else:
        print("Invalid Operator")

    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break
