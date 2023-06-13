

op = input("kg/g? ")

amount = float(input("Amount: "))


if op == "kg":

    print(f"Gramm: {kg * 1000}")
if  op == "g":
    print(f"kg: {amount / 1000}")
