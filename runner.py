from ModifiedRSA import RSA

RSAtool = RSA()
message = RSAtool.write("This is a message")
print(message)
print(RSAtool.read(message))
