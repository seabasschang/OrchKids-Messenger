#Import classes
from ModifiedRSA import RSA
from transmitter import transmitTool
from piglatin import Piglatin
from morsecode import MorseCode
# import your classes here


#Does the initial input, does the user want to read or write?
action = input("Do you want to read or write? ").lower()

#If the user wants to write:
if "write" in action:
    #What is the message the user wants to send?
    message = input("What do you want to send? (Your message) ")
    #Where does the user want to output to?
    output = input("What is the name of the file you want to write into? ")
    #Init of Transmitter class
    tTool = transmitTool(output, "w")

    #Error checking for availability of language translation
    runflag = 1
    while runflag:
        #Input for translation type
        method = input("How do you want to send your message? (RSA, Morse Code or Pig Latin) ").lower()
        #If "rsa", "pig" or "morse" is contained in the method string. [If the user writes "pig latin" or "morse code"], it will work.
        if "rsa" in method:
            #Writing using the RSA object
            RSAtool = RSA()
            translated = RSAtool.write(message)
            tTool.toFile(translated)
            runflag = 0
        elif "pig" in method:
            pigLatinTool = Piglatin()
            translated = pigLatinTool.write(message)
            tTool.toFile(translated)
            runflag = 0
        elif "morse" in method:
            morseCodeTool = MorseCode()
            translated = morseCodeTool.write(message)
            tTool.toFile(translated)
            runflag = 0
        else:
            #Error checking
            print("That was not an option! Please try again!")
    print("Action Completed! Written '" + message + "' to " + output)


#If the user wants to read:
if "read" in action:
    inputmethod = input("Do you want to get your message from a file or input it here? (console or file) ")
    #Input from console
    if "console" in inputmethod:
        #Translated message content
        message = input("What is your message? (Your message) ")

        #Error checking for availability of language translation
        runflag = 1
        while runflag:
            #Same as above
            method = input("What is the type of your message?  (RSA) ").lower()
            if "rsa" in method:
                #Reading using the RSA object
                RSAtool = RSA()
                decoded = RSAtool.read(message)
                print("Message: " + decoded)
                runflag = 0
            else:
                print("That was not an option! Please try again!")
    #Input from file
    else:
        #Location of message
        message = input("What the name of the file that contains your message? ")
        #Set transmitTool object to read from file
        tTool = transmitTool(message, "r")

        #Same as above
        runflag = 1
        while runflag:
            method = input("What is the type of your message?  (RSA) ").lower()
            if "rsa" in method:
                #Reading from file using transmitTool object and outputting to console original text using RSA read function
                RSAtool = RSA()
                decoded = RSAtool.read(tTool.fromFile())
                print("Message: " + decoded)
                runflag = 0
            else:
                print("That was not an option! Please try again!")
