from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

keypair = RSA.generate(1024)

#  public key(e,n) and private key (d,n)

pubKey = keypair.public_key()
pubKeyPEM = pubKey.export_key()
print(pubKeyPEM.decode())

prvKey = keypair.export_key()
print(prvKey.decode())

def encryptMSG(pubKey,m):
    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt(m)
    return encrypted

def decryptMSG():
    pass

def main():
    message = input('give me a message to encrypt: ').encode()
    encrypted = encryptMSG(pubKey,message)
    print(binascii.hexlify(encrypted).decode())

main()