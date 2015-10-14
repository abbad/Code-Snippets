"""
Write a function that accepts a string with some number of consecutive repeating 
characters and returns a copy of the string with consecutive repeating characters 
replaced by a count of the repetitions. 
 
 "sssssTTTTTTops" ? "s5T6ops" 
"""
 
 
def compress_string(string):
	"""
		Function that takes a string and returns a copy of the string with consecutive repeating characters.   
	""" 
	
	compressed_string = ""
	string_pointer = 0
	char_count = 1
	
	if len(string) == 0:
		return ""
	
	while (string_pointer != len(string)):
		# Add character to compressed_string.
		compressed_string += string[string_pointer]
		
		# Increment string pointer.
		string_pointer += 1
		
		while (string_pointer < len(string)):
			# Check next character with the last one added to compressed string array. 
			if (compressed_string[-1] == string[string_pointer]):
				char_count += 1
				string_pointer += 1
				# This if statement is written to handle the last repetition. 
				if len(string) == string_pointer: 
					compressed_string += str(char_count)
			else: 
				# This is used to handle not adding the 1 when the string does not contain repeats. 
				if char_count == 1:
					break
				compressed_string += str(char_count)
				char_count = 1
				break
	
	return compressed_string
		
		