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


#incomplete
class modRSA:

    def write(self, message):

        p = 73
        q = 953

        n = p * q;
        r = (p - 1) * (q - 1)

        k = r + 1;
        while (isprime(k) == True):
            k += r

        e = 1
        d = 0
        for j in range(e + 1, k):
            if k % j == 0:
                if j > e:
                    e = j
                    d = k / j
                    break

        for i in words[z]:
            for j in range(e + 1, k):
                if k % j == 0:
                    if j > e:
                        e = j
                        d = k / j
                        break
            cipher = modpow(ord(i), e, n)
            print(cipher, end = ' ')
