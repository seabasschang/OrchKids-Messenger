from ModifiedRSA import RSA
from transmitter import transmitTool
# import your classes here



action = input("Do you want to read or write? ").lower()
if "write" in action:
    message = input("What do you want to send? ")
    output = input("What is the name of the file you want to write into? ")
    tTool = transmitTool(output, "w")

    runflag = 1
    while runflag:
        method = input("How do you want to send your message? (RSA, Morse or Pig Latin) ").lower()
        if "rsa" in method:
            RSAtool = RSA()
            translated = RSAtool.write(message)
            tTool.toFile(translated)
            runflag = 0
        elif "pig" in method:
            # do your stuff here
            runflag = 0
        elif "morse" in method:
            # do your stuff here
            runflag = 0
        else:
            print("That was not an option! Please try again!")
    print("Action Completed! Written " + message + " to " + output)

if "read" in action:
    inputmethod = input("Do you want to get your message from a file or input it here? (console or file) ")
    if "console" in inputmethod:

        message = input("What is your message? ")
        runflag = 1
        while runflag:
            method = input("What is the type of your message?  (RSA, Morse or Pig Latin) ").lower()
            if "rsa" in method:
                RSAtool = RSA()
                decoded = RSAtool.read(message)
                print("Message: " + decoded)
                runflag = 0
            elif "pig" in method:
                # do your stuff here
                runflag = 0
            elif "morse" in method:
                # do your stuff here
                runflag = 0
            else:
                print("That was not an option! Please try again!")
    else:

        message = input("What the name of the file that contains your message? ")
        tTool = transmitTool(message, "r")

        runflag = 1
        while runflag:
            method = input("What is the type of your message?  (RSA, Morse or Pig Latin) ").lower()
            if "rsa" in method:
                RSAtool = RSA()
                decoded = RSAtool.read(tTool.fromFile())
                print("Message: " + decoded)
                runflag = 0
            elif "pig" in method:
                # do your stuff here
                runflag = 0
            elif "morse" in method:
                # do your stuff here
                runflag = 0
            else:
                print("That was not an option! Please try again!")
