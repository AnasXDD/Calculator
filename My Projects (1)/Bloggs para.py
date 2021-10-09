f = open("kill.txt", "r")
a = f.read()
b=(a.rsplit("\n"))
for i in b:
    print(i+" ", end="")