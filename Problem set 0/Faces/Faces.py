def convert(word):
	new_word = word.replace(":)", "☺").replace( ":(", "😕")
	return new_word
	
def main():
	text = input("type a sentence with emoticon \n")
	converted_word=convert(text)
	print(converted_word)
	
main()

