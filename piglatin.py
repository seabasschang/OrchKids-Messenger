class Piglatin:
	def __init__(self):
		self.consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", 
		"m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z", "'"]
		self.vowels = ["a", "e", "i", "o", "u"]
		self.punct = [".", ",", "?", "!"]
		#Characters sorted as attributes for easy reference.

	def write(self):
		dirty = str(input('Input English Here: ')).lower().split(' ')
		#Split input into array of words.
		clean = ''
		#New "clean" string.
		for l in range(len(dirty)):
		#For each word...
			conso = ''
			#Make a new, empty "conso" for each word.
			if self.vowels.count(dirty[l][0]) == 1 and self.punct.count(dirty[l][-1]) == 1:
				clean += ''+dirty[l][0:-1] +'yay' +dirty[l][-1] +' '
				continue
			#If the vowel-beginning word also ends with a punctuation, make sure to add the punctuation at the end.
			elif self.vowels.count(dirty[l][0]) == 1:
				clean += ''+dirty[l]+'yay '
				continue
			#If the word begins with a vowel and has no punctuation, just add "wordyay_" to clean and skip the rest.
			for n in range(len(dirty[l])):
			#For each letter...
				if self.consonants.count(dirty[l][n]) == 1:
					conso += dirty[l][n]
				#If it is a consonant, add it to the growing "conso" variable and go to next letter.
					if len(conso)+self.punct.count(dirty[l][n]) == len(dirty[l]):
					#If composed of all consonants and punctuation...
						ycase = ''
						for d in range(len(conso)):
						#For each character in the conso...
							go = 1
							if self.consonants.count(conso[d]) == 1 and conso[d] != 'y':
								clean += conso[d]
								ycase += conso[d]
							#If is a following consonant, add it to the sentence and move to the next letter. 
							elif conso[d] == 'y':
								clean += conso[d:] + ycase + 'ay '
								break
							#If it reaches a 'y', add the rest of conso and use the beginning to form an 'ay' suffix.
					continue
				elif self.vowels.count(dirty[l][n]) == 1:
					trunk = str(dirty[l][n:])
					#Define the rest of the word after the first vowel.
					for d in range(len(trunk)):
					#For each character in the remaining word...
						go = 1
						if self.vowels.count(trunk[d]) == 1 or self.consonants.count(trunk[d]) == 1:
							clean += trunk[d]
						#If is a following vowel or consonant, add it to the sentence and move to the next letter. 
						elif self.punct.count(trunk[d]) == 1:
							clean += ''+conso+'ay'+trunk[d]+' '
							go = 0
						#If it is an ending punctuation, add "conso-ay-punct_" to the end and go to the next word.
					if go == 1:
						clean += ''+conso+'ay '
					#If there is no punctuation add "conso-ay_" to the end and go to the next word
					break
		return clean
		#Due to the complexity of the English language, this program does not function properly for all words. 
		#There are many error-checking features, but not enough to catch all inconsistencies.
