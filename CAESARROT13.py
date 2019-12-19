# Run with python3

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

string_input = input("Enter the string: ").upper()

string_output = ""

for i in range(len(string_input)):
	c = string_input[i]
	location = alphabets.find(c)
	new_location = (location + 13)%26
	#if new_location >= 26:
	#	new_location -= 26
	string_output += alphabets[new_location]

print("Encrypted string: ",string_output)
