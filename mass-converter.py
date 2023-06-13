
print("mass converter program")
op = input("kg/g? ")

amount = float(input("Amount: "))


if op == "kg":

    print(f"Gramm: {kg * 1000}")
    print(f"Pounds: {amount * 2.2046}")
elif  op == "g":
    print(f"kg: {amount / 1000}")
