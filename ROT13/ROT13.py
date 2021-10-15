import sys,os

# generating a string that contains all chars:
alpha = ''.join(chr(i) for i in range(65,91))

message = input("enter a message to decrypt: ").upper()

def encryptROT(msg):
    cryped = ''.join(alpha[(alpha.find(i)+13) % 26 ] for i in msg)
    return cryped

# by encrypting the result of the encryptROT function, the result will be the original text

def decryptROT(crypt):
    return encryptROT(crypt)


enc = encryptROT(message)
dec = decryptROT(enc)

print(f"encrypted message= {enc}")
print(f"decrrypted message is {dec}")

##############################################################################

# another version of the two functions:
def encrypt(message):
    encrypted = []
    for i in message:
        if i.isalpha():
            index_of_the_char = alpha.find(i)
            new_index = (index_of_the_char + 13) % 26
            new_value= alpha[new_index]
            encrypted.append(new_value)
        else:
            encrypted.append(i)
    encrypted = ''.join(encrypted)
    return encrypted


def decrypt(message):
    decrypted = []
    for i in message:
        if i.isalpha():
            index_of_the_char = alpha.find(i)
            new_index = (index_of_the_char - 13) % 26
            new_value= alpha[new_index]
            decrypted.append(new_value)
        else:
            decrypted.append(i)
    decrypted = ''.join(decrypted)
    return decrypted

