expression = input("Input an arithmetic expression: \n")
x, y, z = expression.split(" ")
x = float(x)
z = float(z)
y = str(y)
if y == "+":
	print(f"{x + z:.1f}")
elif y == "-":
	print(f"{x - z:.1f}")
elif y == "*":
    print(f"{x * z:.1f}")
elif y == "/":
	print(f"{x / z:.1f}")
else :
	print("invalid operation")
