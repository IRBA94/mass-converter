a = int(input("a: "))
b = int(input("b: "))

op = input("operation: +;-,*,/: ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Error!")
