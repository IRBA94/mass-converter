a = int(input("a: "))
b = int(input("b: "))

op = input("operation: +;-,*,/: ")
file = open("res.txt", "w")
if op == "+":
    file.write(str(a + b))
elif op == "-":
    file.write(str(a - b))
elif op == "*":
    file.write(str(a * b))
elif op == "/":
    try:
        file.write(str(a / b))
    except ZeroDivisionError:
        file.write("Cannot divide 0")
else:
    print("Error!")
file.close()
