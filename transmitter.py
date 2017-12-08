class transmitTool:

    def __init__(self, filename, mode):
        self.f = open(filename, mode)

    def toFile(self,message):
        self.f.write(message)
    def fromFile(self):
        return self.f.read()
