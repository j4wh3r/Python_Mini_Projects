import hashlib
import sys


def crack(hash_file, wordlist):
    result = ""
    with open(hash_file, 'r') as h:
        the_hash = h.readline().rstrip()
        with open(wordlist, "r") as f:
            for line in f.readlines():
                crypt = hashlib.md5()
                line = line.replace("\n","")
                crypt.update(line.encode())
                hashed = crypt.hexdigest()
                if hashed == the_hash:
                    result = f"{the_hash} = {str(line)}"
    if result != "":
        return result
    else:
        return "not found"

def main():
    if len(sys.argv) != 3:
        print("[*]Usage ./hash_file.py hash_file wordlist")
        exit(0)
    hash_file = sys.argv[1]
    wordlist = sys.argv[2]
    result = crack(hash_file, wordlist)
    print(result)

main()

