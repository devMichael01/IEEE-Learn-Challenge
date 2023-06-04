def main():
	word = input("camelCase: ")
	snake_case(word)
	
def snake_case(camel_case):
		for text in camel_case:
			new_word= text.replace(text.upper(), "_"+text.lower()) 
			print(new_word, end="")
	
main()
