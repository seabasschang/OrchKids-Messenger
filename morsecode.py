class MorseCode:
	def write(self, message):
		#When MorseCode is imported into the runner, it takes the message variable from the runner and uses it in the write function
		morse = {'a': '•-', 
				'b': '-•••', 
				'c': '-•-•', 
				'd': '-••', 
				'e': '•', 
				'f': '••-•', 
				'g': '--•', 
				'h': '••••', 
				'i': '••', 
				'j': '•---', 
				'k': '-•-', 
				'l': '•-••', 
				'm': '--', 
				'n': '-•', 
				'o': '---', 
				'p': '•--•', 
				'q': '--•-', 
				'r': '•-•', 
				's': '•••', 
				't':'-', 
				'u': '••-', 
				'v': '•••-', 
				'w': '•--', 
				'x': '-••-', 
				'y': '-•--', 
				'z': '--••',
				' ': ' ',
				'1': '•----',
				'2': '••---',
				'3': '•••--',
				'4': '••••-',
				'5': '•••••',
				'6': '-••••',
				'7': '--•••',
				'8': '---••',
				'9': '----•',
				'0': '-----',
				'.':'•-•-•-',
				',': '••-••',
				'?': '••--••',
				';': '-•-•-',
				':': '---•••'}
		#The morse variable holds the morse code dictionary. It assigns letters, numbers, and punctuation to a series of short and long dashes.

		self.encoded=''
		#self.encoded creates a string to hold the new, encrypted message.
		for i in message:
			#This for loop breaks apart the message from the runner file letter by letter until that message gets entirely rewritten in morse
			self.encoded+=(morse[i.lower()]+'/')
			#i.lower() turns every letter in the message into a lowercase
			#morse[i.lower()] takes the lowercase letter and finds its corresponding set of morse code symbols in the dictionary
			
			#The += adds the morse code symbols into a clean string titled self.encoded
			#In this way, self.encoded acts much like a list that is being appended.
			
			#The '/' at the end of the appendage is neessary because the morse code symbols are confusing when mashed together with no separation
			#For example, •--- could read att or j. Separation between the symbols is necessary: •-/-/-/. Now, it reads att.

		return self.encoded
		#This returns a string to the runner file, but it is now written in morse code.





 