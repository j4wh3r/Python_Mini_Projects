#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser(description="encrypt/decrypt(or bruteforce) strings")
parser.add_argument("-e","--encrypt",type=str,metavar="", help="string to be encrypted")
parser.add_argument("-k","--key",type=int,metavar="",required=True, help="key")
parser.add_argument("-d","--decrypt",type=str,metavar="", help="string to be decrypted")
group = parser.add_mutually_exclusive_group()
group.add_argument("-q", "--quiet", action="store_true", help="print quiet")
group.add_argument("-v", "--verbose", action="store_true", help="print verbose")
args = parser.parse_args()



uppercase = ''.join(chr(i) for i in range(65, 91))
lowercase = ''.join(chr(i) for i in range(97, 123))

def caesar_cipher(text, key):
    c = ""
    for char in text:
        if char in uppercase:
            c += uppercase[(uppercase.find(char) + key) % 26]
        elif char in lowercase:
            c += lowercase[(lowercase.find(char) + key) % 26]
        else:
            c += char
    return c


def caesar_decrypt(cipher, key):
    t = ""
    for char in cipher:
        if char in uppercase:
            t += uppercase[(uppercase.find(char) - key) % 26]
        elif char in lowercase:
            t += lowercase[(lowercase.find(char) - key) % 26]
        else:
            t += char
    return t




if args.decrypt is None:
    encrypted = caesar_cipher(args.encrypt, args.key)
    if args.quiet:
        print(encrypted)
    elif args.verbose:
        print("encrypting the string '%s' using '%d' as a key results to : '%s'" %(args.encrypt,args.key,encrypted))
    else:
          print('"%s" -> "%s"' %(args.encrypt,encrypted))

if args.encrypt is None:
    decrypted = caesar_decrypt(args.decrypt, args.key)
    if args.quiet:
        print(decrypted)
    elif args.verbose:
        print("decrypting the string %s using %d as a key results to : %s" %(args.decrypt,args.key,decrypted))
    else:
        print('"%s" -> "%s"' %(args.decrypt,decrypted))
