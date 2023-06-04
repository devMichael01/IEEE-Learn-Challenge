def main():
	due = 50
	amount =0
	while amount< 50:
		print("Amount due: ", due-amount)
		amount += int(input("insert coin: "))
	print("change owed: ", amount- due)

main()
