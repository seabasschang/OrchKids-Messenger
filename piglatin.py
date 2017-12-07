# consonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
# vowels = ["A", "E", "I", "O", "U"]
def build(prompt)
	dirty = str(input(''+prompt+' ')).lower
	words = []
	word = ""
	for l in range(len(dirty)):
		if dirty[l] != " ":
			word += dirty[l]
		else:
			words.append(word)
	return words

class Piglatin:
	consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
	vowels = ["a", "e", "i", "o", "u"]

	def read(self):
		build('Input Pig Latin Here:')
		

	def write(self):
		build('Input English Here:')