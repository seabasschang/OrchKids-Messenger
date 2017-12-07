import math

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

#incomplete
class RSA:

    def write(self, message):
        self.translated = ""
        p = 73
        q = 953

        self.n = p * q;
        r = (p - 1) * (q - 1)
        k = r + 1;
        while (isprime(k) == True):
            k += r
        e = 1
        self.d = 0
        for j in range(e + 1, k):
            if k % j == 0:
                if j > e:
                    e = j
                    self.d = k / j
                    break
        for i in message:
            cipher = modpow(ord(i), e, self.n)
            self.translated += str(cipher) + ' '
        return self.translated

    def read(self, message):
        arr = message.split()
        self.decoded = ""
        for i in arr:
            self.decoded += chr(modpow(int(i), self.d, self.n))
        return self.decoded
