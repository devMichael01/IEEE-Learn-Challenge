greeting = input("Greet your audience \n")
greeting = greeting.strip()
if greeting.startswith("hello") or greeting.startswith("Hello"):
	print("$0")
elif greeting.startswith("h") or greeting.startswith("H"):
	print("$20")
else:
	print("$100")
