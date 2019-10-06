import sys, operator

# Decrypt a single letter
def decrypt(a, b, letter):
	# ignore spaces, numbers and symbols
	if letter in list("0123456789~`!@#$%^&*()_-+={[}]|\\:;\"'<,>.?/ "): 
		return letter
	# Bruteforce to find inverse of a (need to find better way)
	for i in range(1, 50):
		brute = (a*i) % 26
		if brute == 1:
			a_inv = i
			break
	# Letter's orresponding number
	code = ord(letter.lower()) - 97
	# Decrypted number
	code_dec = (a_inv * (code - b)) % 26
	# Number's corresponding letter
	letter_dec = chr(code_dec + 97)
	return letter_dec

# Check number of occurrences of words in a string, in a word list
def possible_count(words, wordlist):
	count = 0
	for word in words:
		if word in wordlist:
			count += 1
	return count

# Get word list from enable1.txt
with open("enable1.txt", 'r') as f:
	wordlist = set([word.strip() for word in f])

count= list() # for finding most plausible dcryption
for a in [3, 5, 7, 11, 15, 17, 19, 21, 23, 25]:
	for b in range(0, 101):
		encrypted_str = sys.argv[1]
		# perform decrypt function on each letter to get decrypted string
		decrypted_str = "".join([decrypt(a, b, char) for char in encrypted_str])
		# find occurrences in wordlist
		decrypted_str_split = decrypted_str.split(" ")
		word_count = possible_count(decrypted_str_split, wordlist)
		# append occurrences
		count.append([decrypted_str, word_count])


# Sort by occurrences, in descending order
count.sort(key=operator.itemgetter(1), reverse=True)
# Print string with most occurrences
print(count[0][0])
