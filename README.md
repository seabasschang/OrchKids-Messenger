# Messenger by OrchKids

## Description
This masterwork was composed by 3 Choate Rosemary Hall students - Connie Xiao, Sebastian Chang and Zhi Wei Gan. 
The program has the capability to translate/encode messages. It does **RSA** encryption, **Pig Latin** translation as well as **Morse Code** translation.
It also has the capability to read previously translated messages from the file or console and convert it back to the original message.

Run the code, and you will be guided through instructions on how to use the program.

### RSA Class
The RSA class can be initiated with two prime numbers as parameters to generate the private and public key, however they default to 73 and 953.
It has the capability to encode a message using the private key generated with the prime numbers, using the write function. .write(message) returns the encoded string.
It also has the capabiltiy to decode a message using the public key generated with the prime numbers given, using the read function. .read(message) returns the decoded string.

### Transmitter Class
The transmitter class is initiated with a file name and a mode, which determines if it is read or write.
The transmitter class writes a message to the file which the class object was initiated with, using the .toFile(message) function.
The transmitter class can also read a message from the file which the class object was initated with, using the fromFile() function.

### Runner File
The runner file first asks if the user wants to read or write to a file.

For writing:
1. The runner file asks the user for a message which they want to translate and be written to a file.
2. It then asks the name of the file the user wants to write to. If the file does not exist, it is created.
3. It asks what language the user wants to translate into. If the language is not found, it prompts the user again. 

For reading:
1. It asks the user if the message that they want to translate is in a file, or if they would want to take input from the console.
⋅⋅* If console, the program asks what the translated message is, and what type of message it is. It then outputs the original message to the console.
⋅⋅* If from file, the program asks what file the translated message is located, and what type of message it is. It then outputs the original message to the console.

![alt text](https://www.universal-translation-services.com/wp-content/uploads/2016/10/translator-250x250.png "IMAGE")
