# Messenger by OrchKids

## Description
This masterwork was composed by 3 Choate Rosemary Hall students - Connie Xiao, Sebastian Chang and Zhi Wei Gan.
The program has the capability to translate/encode messages. It does **RSA** encryption, **Pig Latin** translation as well as **Morse Code** translation.
It also has the capability to read previously translated messages (in RSA) from the file or console and convert it back to the original message.

Run the code, and you will be guided through instructions on how to use the program.

### RSA Class
The RSA class can be initiated with two prime numbers as parameters to generate the private and public key, however they default to 73 and 953.
It has the capability to encode a message using the private key generated with the prime numbers, using the write function. ***.write(message)*** returns the encoded string.
It also has the capability to decode a message using the public key generated with the prime numbers given, using the read function. ***.read(message)*** returns the decoded string.

### Pig Latin Class
The Pig Latin class is initiated with a set of characters defined as either consonants, vowels, or punctuation.
It has the capability to translate a string of English text into the famous children's code language Pig Latin, using the write function.

As a reminder, Pig Latin takes a string of words,
(ex. "Zhi is great!")
flips them based on the location of the first vowel in the word,
(ex. "izh is eatgr!")
and then adding either "yay" or "ay" to the end of the word.
(ex. "izhay isyay eatgray!")

***.write()*** prompts you to enter English text, and returns the translated text.

Due to the complexity of the English language, and despite the many error-checking features in the code, there are still exceptions that can escape the code. However, the code works for most words and phrases quite well.

### Morse Code Class
The Morse Code class relies on a dictionary of short and long symbols that are assigned to letters, numbers and punctuation. Used in conjunction, these symbols act as an alphabet to write encrypted messages.

The class encodes a message by pairing each letter from the message with a corresponding series of short and long symbols in the morse code dictionary.

For the purposes of this messaging system, the Internation Morse Code language was implemented.

### Transmitter Class
The transmitter class is initiated with a file name and a mode, which determines if it is read or write.
The transmitter class writes a message to the file which the class object was initiated with, using the ***.toFile(message)*** function.
The transmitter class can also read a message from the file which the class object was initated with, using the ***.fromFile()*** function.

### Runner File
The runner file first asks if the user wants to read or write to a file.

For writing:
1. The runner file asks the user for a message which they want to translate and be written to a file.
2. It then asks the name of the file the user wants to write to. If the file does not exist, it is created.
3. It asks what language the user wants to translate into. If the language is not found, it prompts the user again.

For reading:
1. It asks the user if the message that they want to translate is in a file, or if they would want to take input from the console.
  * If console, the program asks what the translated message is, and what type of message it is. It then outputs the original message to the console.
  * If from file, the program asks what file the translated message is located, and what type of message it is. It then outputs the original message to the console.

![alt text](https://www.universal-translation-services.com/wp-content/uploads/2016/10/translator-250x250.png "IMAGE")

### Reflections
**Connie:**
I worked on writing the Morse Code class. Once I had finished that class, I imported it into the runner file and did a few test runs.
In general, each of us worked individually on our separate messaging systems, but then we all contributed to the runner file.
I put most of my work into the Morse Code class and less so into the runner and filing files.

I enjoyed using Github desktop mostly because it centralized everyone's work in one place. I didn't have to scramble to find anyone else's code.
This made it much easier to work on the runner file and send our changes immediately back to the entire group.
The one thing I did find annoying was having to commit changes so often.
When I am doing test runs, I make small corrections, but for each one I think it will be the last correction I need to make.
This is usually not the case, so I end up making multiple commits for changing one small thing.
However, that's a very minor issue. Once you get used to using Github, it seems only logical that you would want to store all of your work there.

**Zhi:**
I worked on the runner file and RSA class. The RSA class was a bit of a challenge because the RSA code I had written beforehand was uncommented and messy. I figured it all out in the end. The importance of commenting really shone through in those moments of facepalm. The runner class was fun to implement because it would have to incorporate everyone's work without their work being completed yet. We planned out how everything came together and we communicated that effectively so everyone knew what they had to do.

I enjoyed practicing my use of GitHub and markdown. I found it very useful to split our work up into different files, because it made it easier to pull and merge, without having to deal with messy pull requests and merging.
