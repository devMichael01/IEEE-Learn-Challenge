def main():
    plate = input("Enter your vanity plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
	if min_length(s) and initial_letter(s) and middle_no(s) and punctuation(s):
		return True
	
def min_length(s):	 	    
	if len(s)>=2 and len(s)<=6:
		return True
	
def initial_letter(s):
	for j in range(len(s)):
		if s[0:2].isalpha():
			return True
	
def middle_no(s):
	i = 2
	for i in range(len(s)):
		while s[i:].isdigit() and s[2] != "0":
			return True
	
def punctuation(s):
	if not s[0:] == [" ", ".", ",", "?", "!", ";", ":", '"']:
		return True
		
main()
