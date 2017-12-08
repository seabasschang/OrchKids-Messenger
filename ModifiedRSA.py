import math
# How it works:
# https://en.wikipedia.org/wiki/RSA_(cryptosystem)


#Utility functions for performing calculations
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def modpow(x,n,m):
  if n == 0:
    return 1
  elif n == 1:
    return x
  elif n%2 == 0:
    return modpow(x*(x%m),n/2,m)%m
  elif n%2 == 1:
    return (x *  modpow(x*(x%m),(n-1)/2,m)%m )%m
def isprime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    else:
        return True

#RSA class
class RSA:

    # e is a public key <-- Everyone can use this key to encrypt the message
    # d is a private key <-- Only the person with the private key can decrypt the message

    #user can use their own primes to generate keys if they want
    #init function creates public and private key
    def __init__(self, prime1 = 73, prime2 = 953):
        self.p = prime1
        self.q = prime2

        self.n = self.p * self.q;
        self.r = (self.p - 1) * (self.q - 1)
        self.k = self.r + 1;
        while (isprime(self.k) == True):
            self.k += self.r
        self.e = 1
        self.d = 0
        for j in range(self.e + 1, self.k):
            if self.k % j == 0:
                if j > self.e:
                    self.e = j
                    self.d = self.k / j
                    break

    #function which encrypts the string, making each character a number which has been encrypted.
    #uses public key to encrypt
    #returns a string of numbers
    def write(self, message):
        self.translated = ""
        for i in message:
            cipher = modpow(ord(i), self.e, self.n)
            self.translated += str(cipher) + ' '
        return self.translated


    #function which decrypts the string, making each number the original character.
    #uses the private key to decrypt
    #returns the string.
    def read(self, message):
        arr = message.split()
        self.decoded = ""
        for i in arr:
            self.decoded += chr(modpow(int(i), self.d, self.n))
        return self.decoded
