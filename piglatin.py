class Piglatin:
	def __init__(self):
		self.consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", 
		"m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
		self.vowels = ["a", "e", "i", "o", "u"]

	def write(self):
		dirty = str(input('Input English Here: ')).lower().split(' ')
		#Split input into array of words.
		clean = ''
		for l in range(len(dirty)):
			conso = ''
			if self.vowels.count(dirty[l][0]) >= 1:
				clean += ''+dirty[l]+'yay '
			for n in range(len(dirty[l])):
				if self.consonants.count(dirty[l][n]) == 1:
					conso += dirty[l][n]
				else:
					stem = str(dirty[l][n-1: -1]) + ''+conso+'ay'
					if l != (len(dirty))-1:
						clean += ''+stem+' '
					else:
						clean += ''+stem+'.'
					break
		return clean

	def read(self):
		build('Input Pig Latin Here:')

reader = Piglatin()
print(reader.write())
