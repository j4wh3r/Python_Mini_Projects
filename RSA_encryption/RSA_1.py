import random

#We will choose the values of p and q for a list composed from prime numbers(from 2 to 50)
def prime(n):
    if n <= 1 :
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            return True

list_of_primes = [i for i in range(2,100) if prime(i) == True] # if the number is prime so we'll append it to the list
# print(f"list of primes = {list_of_primes}")

p = random.choice(list_of_primes)
q = random.choice(list_of_primes)
n = p * q
fi = (p-1) * (q-1)

print(f"p = {p}")
print(f"q = {q}")
print(f"fi = {fi}")
print("n = ",n)


def gcd(x, y):
    while (y):
        x, y = y, x % y

    return x

encryption_exponents = []

for E in range(2,fi):
    if gcd(E,fi) == 1:
        encryption_exponents.append(E)
# print(encryption_exponents)

# e = random.choice(encryption_exponents)
e = encryption_exponents[0]
print("e = ",e)

# calculating the d

d = 0
count = 0
d_l = []
while True:
    if e * d % fi == 1:
        d_l.append(d)
        d = d_l[0]
        print("d = ",d)
        break
    d+= 1


message = int(input("enter a message: "))

def cryptRSA(m,e,n):
    c  = (m ** e) % n
    print("cipher message = ",c)
    return c

def decryptRSA(c,d,n):
    if  d is not None:
        t = (c ** d) % n
        print("original message is : ",t)
    else:
        print("oh no !!")

c = cryptRSA(message,e,n)
decryptRSA(c,d,n)

