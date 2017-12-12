#Transmitter class
class transmitTool:
    #Initialiaze object with the name of the file, and the mode (read or write)
    #The modes are the default python modes, so writing to a file is "w" and reading is "r"
    #Sets file object within transmitTool object
    def __init__(self, filename, mode):
        self.f = open(filename, mode)

    #writes message to file provided in init.
    def toFile(self,message):
        self.f.write(message)
    #reads message from file provided in init, returns content.
    def fromFile(self):
        return self.f.read()
