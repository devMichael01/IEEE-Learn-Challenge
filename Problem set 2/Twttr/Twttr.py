def main():
	word= input("input word: ")
	remove_vowel(word)
	
def remove_vowel(text):
	vowel = {"a", "e", "i", "o", "u"}
	for letter in text:	
		if letter in vowel: 
			new_word = text.replace("a", "").replace( "e",  "").replace("i", "").replace( " o", "").replace( "u", "")
	print(new_word)
main()	
